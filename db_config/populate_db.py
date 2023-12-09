import pandas as pd
from config import sales_eod_path, transactions
from db_config.config import engine, Session

from db_config.models import Transactions


def populate():
    sales_eod_pathDf = pd.read_excel(sales_eod_path)
    transactionsDf = pd.read_excel(transactions)

    sales_eod_pathDf.to_sql('sales_and_eod_stocks', engine, index=False, if_exists = 'replace')
    transactionsDf.to_sql('sales_and_eod_stocks', engine, index=False, if_exists = 'replace')

    session = Session()
    print(session.query(Transactions).all())
