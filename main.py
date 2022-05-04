import uvicorn
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory='templates')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/points/", response_model=list[schemas.Point])
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_points(db, skip=skip, limit=limit)


@app.post("/points/", response_model=schemas.Point)
def create_point(point: schemas.Point, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point.id)
    if db_point:
        raise HTTPException(status_code=400, detail="Point already exist")
    return crud.create_point(db, point)


@app.put("/points/", response_model=schemas.Point)
def change_point(point: schemas.Point, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point.id)
    if not db_point:
        raise HTTPException(status_code=400, detail="Point not exist")
    return crud.change_point(db, point)


@app.delete("/points/", response_model=schemas.Point)
def delete_point(point_id: int, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point_id)
    if not db_point:
        raise HTTPException(status_code=400, detail="Point not exist")
    return crud.delete_point(db, db_point)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
