from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.expense import Expense


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        nullable=False,
    )

    categories: Mapped[list[Category]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    expenses: Mapped[list[Expense]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )