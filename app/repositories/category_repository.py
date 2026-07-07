from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    @staticmethod
    def get_all(db: Session, user_id: int):
        return (
            db.query(Category)
            .filter(Category.user_id == user_id)
            .order_by(Category.name)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        category_id: int,
        user_id: int,
    ):
        return (
            db.query(Category)
            .filter(
                Category.id == category_id,
                Category.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def get_by_name(
        db: Session,
        name: str,
        user_id: int,
    ):
        return (
            db.query(Category)
            .filter(
                Category.name == name,
                Category.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        category: Category,
    ):
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def delete(
        db: Session,
        category: Category,
    ):
        db.delete(category)
        db.commit()