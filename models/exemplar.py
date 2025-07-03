from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()

class Exemplar(Base):
    __tablename__ = "exemplar"
    tombo: Mapped[int] = mapped_column(primary_key=True)
    codigo_livro: Mapped[int] = mapped_column(ForeignKey("livro.codigo"))