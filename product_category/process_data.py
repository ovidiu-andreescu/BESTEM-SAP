import pandas as pd

from db_config.config import Session

session = Session()

data_df = pd.read_sql(session.query())