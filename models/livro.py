from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()

class Livro(Base):
    __tablename__ = "livro"
    codigo: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    autor: Mapped[str]
    editora: Mapped[str]
    ano: Mapped[int]