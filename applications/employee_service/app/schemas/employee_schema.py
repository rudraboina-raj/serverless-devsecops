from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate


class EmployeeRequestSchema(Schema):

    first_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
    )

    last_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
    )

    email = fields.Email(required=True)

    department = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
    )

    designation = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
    )

    salary = fields.Float(
        required=True,
        validate=validate.Range(min=1),
    )


class EmployeeResponseSchema(Schema):

    employee_id = fields.String()

    first_name = fields.String()

    last_name = fields.String()

    email = fields.Email()

    department = fields.String()

    designation = fields.String()

    salary = fields.Float()