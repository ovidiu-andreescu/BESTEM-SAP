import pandas as pd
from db_config.config import Session
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from db_config.models import SalesAndEod
import numpy as np

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

    forecast = results.get_forecast(steps=15)
    forecast_values = forecast.predicted_mean
    forecast_conf_int = forecast.conf_int()

    historical_residuals = df['Sales'] - results.fittedvalues

    std_dev = np.std(historical_residuals)

    threshold = 2 * std_dev


    potential_anomalies = forecast_values[abs(forecast_values - df['Sales'].mean()) > threshold]

    anomaly_dates = [date - pd.DateOffset(days=3) for date in potential_anomalies.index if
                     date > df.index.min() + pd.DateOffset(days=3)]

    if not anomaly_dates:
        print("No anomalies detected 3 days in advance.")
    else:
        print("Anomaly Dates (3 days in advance):", anomaly_dates)

