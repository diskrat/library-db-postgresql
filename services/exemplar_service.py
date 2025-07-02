
from sqlalchemy.orm import Session
from models import Exemplar

def create_exemplar(db: Session, exemplar_data: dict) -> Exemplar:
    exemplar = Exemplar(**exemplar_data)
    db.add(exemplar)
    db.commit()
    db.refresh(exemplar)
    return exemplar

def get_exemplar(db: Session, tombo: int) -> Exemplar | None:
    return db.query(Exemplar).filter(Exemplar.tombo == tombo).first()

def get_exemplares(db: Session, skip: int = 0, limit: int = 100) -> list[Exemplar]:
    return db.query(Exemplar).offset(skip).limit(limit).all()

def update_exemplar(db: Session, tombo: int, update_data: dict) -> Exemplar | None:
    exemplar = db.query(Exemplar).filter(Exemplar.tombo == tombo).first()
    if exemplar:
        for key, value in update_data.items():
            setattr(exemplar, key, value)
        db.commit()
        db.refresh(exemplar)
    return exemplar

def delete_exemplar(db: Session, tombo: int) -> bool:
    exemplar = db.query(Exemplar).filter(Exemplar.tombo == tombo).first()
    if exemplar:
        db.delete(exemplar)
        db.commit()
        return True
    return False
