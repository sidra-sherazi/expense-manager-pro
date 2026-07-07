from __future__ import annotations
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.expense import Expense


class Category(Base):
    __tablename__ = "categories"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "name",
            name="uq_user_category_name",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="categories",
    )

    expenses: Mapped[list["Expense"]] = relationship(
        "Expense",
        back_populates="category",
        cascade="all, delete-orphan",
    )