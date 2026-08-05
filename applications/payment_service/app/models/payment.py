from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String

from shared.database.base import Base


class Payment(Base):

    __tablename__ = "payments"

    payment_id = Column(String, primary_key=True)

    order_id = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    payment_method = Column(String, nullable=False)

    status = Column(String, nullable=False)