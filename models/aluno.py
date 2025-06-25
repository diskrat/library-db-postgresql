from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Aluno(Base):
    __tablename__ = "user_account"
    matricula: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str]
    curso: Mapped[str]

class Livro(Base):
    __tablename__ = "livro"
    codigo: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    autor: Mapped[str]
    editora: Mapped[str]
    ano_publicacao: Mapped[int]

class Exemplar(Base):
    __tablename__ = "exemplar"
    tombo: Mapped[int] = mapped_column(primary_key=True)
    codigo_livro: Mapped[int] = mapped_column(ForeignKey("livro.codigo"))

class Emprestimo(Base):
    __tablename__ = "emprestimo"
    codigo: Mapped[int] = mapped_column(primary_key=True)
    data_emprestimo: Mapped[date]
    data_prev_devolucao: Mapped[date]
    data_devolucao: Mapped[date]
    matricula_aluno: Mapped[int] = mapped_column(ForeignKey("aluno.matricula"))

class EmprestimoExemplar(Base):
    __tablename__ = "emprestimo_exemplar"
    codigo_emprestimo: Mapped[int] = mapped_column(ForeignKey("emprestimo.codigo"))
    tombo_exemplar: Mapped[int] = mapped_column(ForeignKey("exemplar.tombo"))

    