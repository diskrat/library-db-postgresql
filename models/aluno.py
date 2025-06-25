from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "aluno"
    matricula: Mapped[int] = mapped_column(ForeignKey("aluno.matricula"), primary_key=True)
    nome: Mapped[str]
    email: Mapped[str]
    curso: Mapped[str]