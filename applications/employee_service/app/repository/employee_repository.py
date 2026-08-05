from sqlalchemy.orm import Session

from ..models.employee import Employee


class EmployeeRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, employee: Employee):
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def find_by_email(self, email):
        return (
            self.db.query(Employee)
            .filter(Employee.email == email)
            .first()
        )

    def find_all(self):
        return self.db.query(Employee).all()

    def find_by_employee_id(self, employee_id):
        return (
            self.db.query(Employee)
            .filter(Employee.employee_id == employee_id)
            .first()
        )

    def update(self, employee):
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete(self, employee):
        self.db.delete(employee)
        self.db.commit()