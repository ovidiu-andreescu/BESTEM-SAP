import os
# from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

sales_eod_path = os.path.join(ROOT_DIR, 'sales_and_eodStocks.xlsx')
transactions = os.path.join(ROOT_DIR, 'transactions.xlsx')
conf_path = os.path.join(ROOT_DIR, 'application.conf')

ma = Marshmallow()