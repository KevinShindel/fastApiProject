from sqlalchemy.orm import Session

from sql_app import models, schemas


def get_point(db: Session, point_id: int):
    return db.query(models.Point).get(point_id)


def get_points(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Point).offset(skip).limit(limit).all()


def create_point(db: Session, point: schemas.Point):
    db_point = models.Point(**point.dict())
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


def change_point(db: Session, point: schemas.Point):
    db_point = models.Point(**point.dict())
    db.query(models.Point).update(point.dict())
    db.commit()
    return db_point


def delete_point(db: Session, point: schemas.Point):
    db.delete(point)
    db.commit()
    return True
