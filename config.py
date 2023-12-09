import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

sales_eod_path = os.path.join(ROOT_DIR, 'sales_and_eodStocks.xlsx')
transactions = os.path.join(ROOT_DIR, 'transactions.xlsx')
conf_path = os.path.join(ROOT_DIR, 'application.conf')