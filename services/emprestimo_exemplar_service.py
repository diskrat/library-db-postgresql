from sqlalchemy.orm import Session
from models import EmprestimoExemplar

def create_emprestimo_exemplar(db: Session, emprestimo_exemplar_data: dict) -> EmprestimoExemplar:
    emprestimo_exemplar = EmprestimoExemplar(**emprestimo_exemplar_data)
    db.add(emprestimo_exemplar)
    db.commit()
    db.refresh(emprestimo_exemplar)
    return emprestimo_exemplar

def get_emprestimo_exemplar(db: Session, codigo_emprestimo: int, tombo_exemplar: int) -> EmprestimoExemplar | None:
    return db.query(EmprestimoExemplar).filter(
        EmprestimoExemplar.codigo_emprestimo == codigo_emprestimo,
        EmprestimoExemplar.tombo_exemplar == tombo_exemplar
    ).first()

def get_emprestimo_exemplares(db: Session, skip: int = 0, limit: int = 100) -> list[EmprestimoExemplar]:
    return db.query(EmprestimoExemplar).offset(skip).limit(limit).all()

def update_emprestimo_exemplar(db: Session, codigo_emprestimo: int, tombo_exemplar: int, update_data: dict) -> EmprestimoExemplar | None:
    emprestimo_exemplar = get_emprestimo_exemplar(db, codigo_emprestimo, tombo_exemplar)
    if emprestimo_exemplar:
        for key, value in update_data.items():
            setattr(emprestimo_exemplar, key, value)
        db.commit()
        db.refresh(emprestimo_exemplar)
    return emprestimo_exemplar

def delete_emprestimo_exemplar(db: Session, codigo_emprestimo: int, tombo_exemplar: int) -> bool:
    emprestimo_exemplar = get_emprestimo_exemplar(db, codigo_emprestimo, tombo_exemplar)
    if emprestimo_exemplar:
        db.delete(emprestimo_exemplar)
        db.commit()
        return True
    return False
