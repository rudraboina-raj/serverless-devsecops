import uuid

from shared.messaging import PubSubPublisher

from ..models.employee import Employee
from ..repository.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self, repository: EmployeeRepository):

        self.repository = repository

        self.publisher = PubSubPublisher()

    def create_employee(
        self,
        first_name,
        last_name,
        email,
        department,
        designation,
        salary,
    ):

        if self.repository.find_by_email(email):
            raise ValueError("Employee with this email already exists.")

        employee = Employee(
            employee_id=str(uuid.uuid4()),
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            designation=designation,
            salary=salary,
        )

        employee = self.repository.save(employee)

        self.publisher.publish(
            {
                "event": "EmployeeCreated",
                "employee_id": employee.employee_id,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "email": employee.email,
                "department": employee.department,
                "designation": employee.designation,
            }
        )

        return employee

    def get_all_employees(self):

        return self.repository.find_all()

    def get_employee(self, employee_id):

        employee = self.repository.find_by_employee_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        return employee

    def update_employee(
        self,
        employee_id,
        department,
        designation,
        salary,
    ):

        employee = self.repository.find_by_employee_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        employee.department = department
        employee.designation = designation
        employee.salary = salary

        return self.repository.update(employee)

    def delete_employee(self, employee_id):

        employee = self.repository.find_by_employee_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        self.repository.delete(employee)