import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


# @app.get(path="/", status_code=200)
# async def root():
#     return {"message": "ok"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get('/maps', status_code=200)
async def maps(request):
    return templates.TemplateResponse(name='index.html', context={"request": request})


@app.get("/html/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
