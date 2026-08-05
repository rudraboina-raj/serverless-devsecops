from sqlalchemy.orm import Session

from ..models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def find_by_sku(self, sku):
        return self.db.query(Product).filter(Product.sku == sku).first()

    def find_all(self):
        return self.db.query(Product).all()

    def find_by_product_id(self, product_id):
        return self.db.query(Product).filter(Product.product_id == product_id).first()

    def update(self, product):
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product):
        self.db.delete(product)
        self.db.commit()
