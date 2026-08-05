from sqlalchemy.orm import Session

from applications.payment_service.app.models.payment import Payment


class PaymentRepository:

    @staticmethod
    def create(db: Session, payment: Payment):

        db.add(payment)

        db.commit()

        db.refresh(payment)

        return payment

    @staticmethod
    def get_all(db: Session):

        return db.query(Payment).all()

    @staticmethod
    def get_by_id(db: Session, payment_id: str):

        return db.query(Payment).filter(Payment.payment_id == payment_id).first()

    @staticmethod
    def update(db: Session, payment: Payment):

        db.commit()

        db.refresh(payment)

        return payment
