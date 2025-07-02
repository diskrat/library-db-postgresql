from sqlalchemy import ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import date

Base = declarative_base()

class EmprestimoExemplar(Base):
    __tablename__ = "empr_exemplar"
    codigo_emprestimo: Mapped[int] = mapped_column(ForeignKey("emprestimo.codigo"))
    tombo_exemplar: Mapped[int] = mapped_column(ForeignKey("exemplar.tombo"))
    data_devolucao: Mapped[Optional[date]] = mapped_column(default=None)
    dias_atraso: Mapped[Optional[int]] = mapped_column(default=None)