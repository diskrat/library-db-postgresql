
from sqlalchemy.orm import Session
from models import Emprestimo

def create_emprestimo(db: Session, emprestimo_data: dict) -> Emprestimo:
    emprestimo = Emprestimo(**emprestimo_data)
    db.add(emprestimo)
    db.commit()
    db.refresh(emprestimo)
    return emprestimo

def get_emprestimo(db: Session, codigo: int) -> Emprestimo | None:
    return db.query(Emprestimo).filter(Emprestimo.codigo == codigo).first()

def get_emprestimos(db: Session, skip: int = 0, limit: int = 100) -> list[Emprestimo]:
    return db.query(Emprestimo).offset(skip).limit(limit).all()

def update_emprestimo(db: Session, codigo: int, update_data: dict) -> Emprestimo | None:
    emprestimo = db.query(Emprestimo).filter(Emprestimo.codigo == codigo).first()
    if emprestimo:
        for key, value in update_data.items():
            setattr(emprestimo, key, value)
        db.commit()
        db.refresh(emprestimo)
    return emprestimo

def delete_emprestimo(db: Session, codigo: int) -> bool:
    emprestimo = db.query(Emprestimo).filter(Emprestimo.codigo == codigo).first()
    if emprestimo:
        db.delete(emprestimo)
        db.commit()
        return True
    return False
