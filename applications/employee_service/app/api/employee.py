from flask import Blueprint, request, jsonify

from marshmallow import ValidationError

from shared.database.connection import SessionLocal

from ..repository.employee_repository import EmployeeRepository
from ..services.employee_service import EmployeeService
from ..schemas.employee_schema import (
    EmployeeRequestSchema,
    EmployeeResponseSchema,
)


employee_bp = Blueprint("employee", __name__)


# -------------------------------------------------------
# Create Employee
# -------------------------------------------------------
@employee_bp.route("/employees", methods=["POST"])
def create_employee():

    data = request.get_json()

    request_schema = EmployeeRequestSchema()

    db = None

    try:

        # Validate request body
        data = request_schema.load(data)

        db = SessionLocal()

        repository = EmployeeRepository(db)

        service = EmployeeService(repository)

        employee = service.create_employee(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            department=data["department"],
            designation=data["designation"],
            salary=data["salary"],
        )

        return jsonify(
            {
                "message": "Employee created successfully",
                "employee_id": employee.employee_id,
            }
        ), 201

    except ValidationError as err:

        return jsonify(
            {
                "errors": err.messages
            }
        ), 400

    except ValueError as e:

        return jsonify(
            {
                "error": str(e)
            }
        ), 400

    except Exception as e:

        return jsonify(
            {
                "error": "Internal Server Error",
                "details": str(e)
            }
        ), 500

    finally:

        if db:
            db.close()


# -------------------------------------------------------
# Get All Employees
# -------------------------------------------------------
# -------------------------------------------------------
# Get All Employees
# -------------------------------------------------------
@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    db = SessionLocal()

    try:

        repository = EmployeeRepository(db)

        service = EmployeeService(repository)

        employees = service.get_all_employees()

        response_schema = EmployeeResponseSchema(many=True)

        return jsonify(
            response_schema.dump(employees)
        ), 200

    except Exception as e:

        return jsonify(
            {
                "error": "Internal Server Error",
                "details": str(e)
            }
        ), 500

    finally:

        db.close()


# -------------------------------------------------------
# Get Employee By ID
# -------------------------------------------------------
# -------------------------------------------------------
# Get Employee By ID
# -------------------------------------------------------
@employee_bp.route("/employees/<employee_id>", methods=["GET"])
def get_employee(employee_id):

    db = SessionLocal()

    try:

        repository = EmployeeRepository(db)

        service = EmployeeService(repository)

        employee = service.get_employee(employee_id)

        response_schema = EmployeeResponseSchema()

        return jsonify(
            response_schema.dump(employee)
        ), 200

    except ValueError as e:

        return jsonify(
            {
                "error": str(e)
            }
        ), 404

    finally:

        db.close()


# -------------------------------------------------------
# Update Employee
# -------------------------------------------------------
@employee_bp.route("/employees/<employee_id>", methods=["PUT"])
def update_employee(employee_id):

    data = request.get_json()

    db = SessionLocal()

    try:

        repository = EmployeeRepository(db)

        service = EmployeeService(repository)

        employee = service.update_employee(
            employee_id=employee_id,
            department=data["department"],
            designation=data["designation"],
            salary=data["salary"],
        )

        return jsonify(
            {
                "message": "Employee updated successfully",
                "employee_id": employee.employee_id,
            }
        ), 200

    except ValueError as e:

        return jsonify(
            {
                "error": str(e)
            }
        ), 404

    finally:

        db.close()


# -------------------------------------------------------
# Delete Employee
# -------------------------------------------------------
@employee_bp.route("/employees/<employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    db = SessionLocal()

    try:

        repository = EmployeeRepository(db)

        service = EmployeeService(repository)

        service.delete_employee(employee_id)

        return jsonify(
            {
                "message": "Employee deleted successfully"
            }
        ), 200

    except ValueError as e:

        return jsonify(
            {
                "error": str(e)
            }
        ), 404

    finally:

        db.close()