from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from db_config.config import Base


class Transactions(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    invoice = Column(Integer)
    product_id = Column(String, ForeignKey('sales_and_eod_stocks.product_id'))
    description = Column(String)
    quantity = Column(Integer)
    date = Column(DateTime)
    price = Column(Float)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    country = Column(String)

    sales_and_eod = relationship('SalesAndEod', backref='transactions')
    customer = relationship('Customers', back_populates='transactions')


class SalesAndEod(Base):
    __tablename__ = 'sales_and_eod_stocks'

    product_id_number = Column(Integer, primary_key=True)
    product_id = Column(String)
    date = Column(DateTime)
    sales = Column(Integer)
    revenue = Column(Float)
    end_of_day_stock = Column(Integer)


class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    email = Column(String)

    transactions = relationship('Transactions', back_populates='customer')