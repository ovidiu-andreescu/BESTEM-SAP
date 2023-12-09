from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from db_config.config import Base


class Transactions(Base):
    __tablename__ = 'transactions'

    Transaction_ID = Column(Integer, primary_key=True)
    Invoice = Column(Integer)
    Product_ID = Column(String, ForeignKey('sales_and_eod_stocks.Product_ID'))
    Description = Column(String)
    Quantity = Column(Integer)
    Date = Column(DateTime)
    Price = Column(Float)
    Customer_ID = Column(Integer, ForeignKey('customers.Customer_ID'))
    Country = Column(String)

    sales_and_eod = relationship('SalesAndEod', backref='transactions')
    customer = relationship('Customers', back_populates='transactions')


class SalesAndEod(Base):
    __tablename__ = 'sales_and_eod_stocks'

    Product_ID_number = Column(Integer, primary_key=True)
    Product_ID = Column(String)
    Date = Column(DateTime)
    Sales = Column(Integer)
    Revenue = Column(Float)
    EndOfDayStock = Column(Integer)


class Customers(Base):
    __tablename__ = 'customers'

    Customer_ID = Column(Integer, primary_key=True)
    Email = Column(String)

    transactions = relationship('Transactions', back_populates='customer')