from flask import Blueprint, request, jsonify

from marshmallow import ValidationError

from shared.database.connection import SessionLocal

from ..repository.product_repository import ProductRepository
from ..services.product_service import ProductService
from ..schemas.product import (
    ProductRequestSchema,
    ProductResponseSchema,
)

product_bp = Blueprint("product", __name__)


# -------------------------------------------------------
# Create Product
# -------------------------------------------------------
@product_bp.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    request_schema = ProductRequestSchema()

    db = None

    try:

        data = request_schema.load(data)

        db = SessionLocal()

        repository = ProductRepository(db)

        service = ProductService(repository)

        product = service.create_product(
            product_name=data["product_name"],
            description=data.get("description"),
            category=data["category"],
            sku=data["sku"],
            price=data["price"],
            quantity=data["quantity"],
        )

        return jsonify(
            {
                "message": "Product created successfully",
                "product_id": product.product_id,
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
# Get All Products
# -------------------------------------------------------
@product_bp.route("/products", methods=["GET"])
def get_products():

    db = SessionLocal()

    try:

        repository = ProductRepository(db)

        service = ProductService(repository)

        products = service.get_all_products()

        response_schema = ProductResponseSchema(many=True)

        return jsonify(
            response_schema.dump(products)
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
# Get Product By ID
# -------------------------------------------------------
@product_bp.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):

    db = SessionLocal()

    try:

        repository = ProductRepository(db)

        service = ProductService(repository)

        product = service.get_product(product_id)

        response_schema = ProductResponseSchema()

        return jsonify(
            response_schema.dump(product)
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
# Update Product
# -------------------------------------------------------
@product_bp.route("/products/<product_id>", methods=["PUT"])
def update_product(product_id):

    data = request.get_json()

    db = SessionLocal()

    try:

        repository = ProductRepository(db)

        service = ProductService(repository)

        product = service.update_product(
            product_id=product_id,
            category=data["category"],
            price=data["price"],
            quantity=data["quantity"],
        )

        return jsonify(
            {
                "message": "Product updated successfully",
                "product_id": product.product_id,
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
# Delete Product
# -------------------------------------------------------
@product_bp.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):

    db = SessionLocal()

    try:

        repository = ProductRepository(db)

        service = ProductService(repository)

        service.delete_product(product_id)

        return jsonify(
            {
                "message": "Product deleted successfully"
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