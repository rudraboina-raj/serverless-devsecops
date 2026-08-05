from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from shared.database.base import Base


class Order(Base):

    __tablename__ = "orders"

    order_id = Column(
        String,
        primary_key=True,
    )

    employee_id = Column(
        String,
        nullable=False,
    )

    product_id = Column(
        String,
        nullable=False,
    )

    quantity = Column(
        Integer,
        nullable=False,
    )

    total_price = Column(
        Float,
        nullable=False,
    )

    status = Column(
        String,
        nullable=False,
        default="CREATED",
    )
