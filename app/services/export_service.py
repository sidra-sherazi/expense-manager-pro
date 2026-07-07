import csv
import os
from tempfile import NamedTemporaryFile

from openpyxl import Workbook
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.export_repository import ExportRepository


class ExportService:

    @staticmethod
    def export_csv(
        db: Session,
        user: User,
    ):

        expenses = ExportRepository.get_expenses(
            db=db,
            user_id=user.id,
        )

        temp = NamedTemporaryFile(
            delete=False,
            suffix=".csv",
            mode="w",
            newline="",
            encoding="utf-8",
        )

        writer = csv.writer(temp)

        writer.writerow([
            "Title",
            "Amount",
            "Category",
            "Description",
            "Created At",
        ])

        for expense in expenses:
            writer.writerow([
                expense.title,
                expense.amount,
                expense.category,
                expense.description,
                expense.created_at,
            ])

        temp.close()

        return temp.name

    @staticmethod
    def export_excel(
        db: Session,
        user: User,
    ):

        expenses = ExportRepository.get_expenses(
            db=db,
            user_id=user.id,
        )

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Expenses"

        sheet.append([
            "Title",
            "Amount",
            "Category",
            "Description",
            "Created At",
        ])

        for expense in expenses:
            sheet.append([
                expense.title,
                expense.amount,
                expense.category,
                expense.description,
                str(expense.created_at),
            ])

        temp = NamedTemporaryFile(
            delete=False,
            suffix=".xlsx",
        )

        workbook.save(temp.name)

        return temp.name