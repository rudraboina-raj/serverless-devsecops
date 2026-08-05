from ..models.product import Product
from ..repository.product_repository import ProductRepository


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(
        self,
        product_name,
        description,
        category,
        sku,
        price,
        quantity,
    ):

        if self.repository.find_by_sku(sku):
            raise ValueError("Product with this SKU already exists.")

        product = Product(
            product_name=product_name,
            description=description,
            category=category,
            sku=sku,
            price=price,
            quantity=quantity,
        )

        return self.repository.save(product)

    def get_all_products(self):
        return self.repository.find_all()

    def get_product(self, product_id):

        product = self.repository.find_by_product_id(product_id)

        if product is None:
            raise ValueError("Product not found.")

        return product

    def update_product(
        self,
        product_id,
        category,
        price,
        quantity,
    ):

        product = self.repository.find_by_product_id(product_id)

        if product is None:
            raise ValueError("Product not found.")

        product.category = category
        product.price = price
        product.quantity = quantity

        return self.repository.update(product)

    def delete_product(self, product_id):

        product = self.repository.find_by_product_id(product_id)

        if product is None:
            raise ValueError("Product not found.")

        self.repository.delete(product)
