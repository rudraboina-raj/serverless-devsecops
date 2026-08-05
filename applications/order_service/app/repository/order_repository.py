from sqlalchemy.orm import Session

from ..models.order import Order


class OrderRepository:

    @staticmethod
    def create(db: Session, order: Order):

        db.add(order)

        db.commit()

        db.refresh(order)

        return order

    @staticmethod
    def get_by_id(db: Session, order_id: str):

        return db.query(Order).filter(Order.order_id == order_id).first()

    @staticmethod
    def get_all(db: Session):

        return db.query(Order).all()
