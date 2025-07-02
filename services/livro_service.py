
from sqlalchemy.orm import Session
from models import Livro

def create_livro(db: Session, livro_data: dict) -> Livro:
    livro = Livro(**livro_data)
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro

def get_livro(db: Session, codigo: int) -> Livro | None:
    return db.query(Livro).filter(Livro.codigo == codigo).first()

def get_livros(db: Session, skip: int = 0, limit: int = 100) -> list[Livro]:
    return db.query(Livro).offset(skip).limit(limit).all()

def update_livro(db: Session, codigo: int, update_data: dict) -> Livro | None:
    livro = db.query(Livro).filter(Livro.codigo == codigo).first()
    if livro:
        for key, value in update_data.items():
            setattr(livro, key, value)
        db.commit()
        db.refresh(livro)
    return livro

def delete_livro(db: Session, codigo: int) -> bool:
    livro = db.query(Livro).filter(Livro.codigo == codigo).first()
    if livro:
        db.delete(livro)
        db.commit()
        return True
    return False
