from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import date

Base = declarative_base()

class Emprestimo(Base):
    __tablename__ = "emprestimo"
    codigo: Mapped[int] = mapped_column(ForeignKey("emprestimo.codigo"), primary_key=True)
    data_emprestimo: Mapped[date]
    data_prev_dev: Mapped[date]
    matricula_aluno: Mapped[int] = mapped_column(ForeignKey("aluno.matricula"))