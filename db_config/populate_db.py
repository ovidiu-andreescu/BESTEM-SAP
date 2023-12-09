import pandas as pd
from config import sales_eod_path, transactions
from db_config.config import engine, Session

from db_config.models import Transactions


def populate():
    sales_eod_path_df = pd.read_excel(sales_eod_path)
    transactions_df = pd.read_excel(transactions)

    sales_eod_path_df.to_sql('sales_and_eod_stocks', engine, index=False, if_exists = 'replace')
    transactions_df.to_sql('transactions', engine, index=False, if_exists = 'replace')