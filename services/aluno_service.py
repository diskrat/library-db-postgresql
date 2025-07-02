from sqlalchemy.orm import Session

from models import Aluno

def create_aluno(db: Session, aluno_data: dict) -> Aluno:
    aluno = Aluno(**aluno_data)
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno

def get_aluno(db: Session, matricula: int) -> Aluno | None:
    return db.query(Aluno).filter(Aluno.matricula == matricula).first()

def get_alunos(db: Session, skip: int = 0, limit: int = 100) -> list[Aluno]:
    return db.query(Aluno).offset(skip).limit(limit).all()

def update_aluno(db: Session, matricula: int, update_data: dict) -> Aluno | None:
    aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
    if aluno:
        for key, value in update_data.items():
            setattr(aluno, key, value) 
        db.commit()
        db.refresh(aluno)
    return aluno

def delete_aluno(db: Session, matricula: int) -> bool:
    aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
    if aluno:
        db.delete(aluno)
        db.commit()
        return True
    return False