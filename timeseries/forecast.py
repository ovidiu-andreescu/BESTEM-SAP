import pandas as pd
from db_config.config import Session
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from db_config.models import SalesAndEod

def predict_sales():
    session = Session()
    data = pd.DataFrame(session.query(SalesAndEod.Date, SalesAndEod.Sales))

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    if df.index.duplicated().any():
        df = df.groupby(df.index).sum()

    all_dates = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
    df = df.reindex(all_dates, fill_value=0)

    result = adfuller(df['Sales'])

    if result[1] > 0.05:
        df['Sales'] = df['Sales'].diff().dropna()

    model = SARIMAX(df['Sales'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit()

    forecast = results.forecast(steps=12)

    return forecast
