from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate


class ProductRequestSchema(Schema):

    product_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=150),
    )

    description = fields.String(
        required=False,
        allow_none=True,
    )

    category = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
    )

    sku = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100),
    )

    price = fields.Float(
        required=True,
        validate=validate.Range(min=0),
    )

    quantity = fields.Integer(
        required=True,
        validate=validate.Range(min=0),
    )


class ProductResponseSchema(Schema):

    id = fields.Integer()

    product_name = fields.String()

    description = fields.String()

    category = fields.String()

    sku = fields.String()

    price = fields.Float()

    quantity = fields.Integer()
