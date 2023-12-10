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

    # Assuming 'results' is your fitted SARIMAX model and 'df' is your DataFrame
    forecast = results.get_forecast(steps=15)
    forecast_values = forecast.predicted_mean

    historical_residuals = df['Sales'] - results.fittedvalues

    std_dev = np.std(historical_residuals)

    threshold = 2 * std_dev

    historical_anomalies = df['Sales'][abs(historical_residuals) > threshold]

    future_anomalies = forecast_values[abs(forecast_values - df['Sales'].mean()) > threshold]

    advance_alerts = [date - pd.DateOffset(days=3) for date in future_anomalies.index if
                      date > df.index.min() + pd.DateOffset(days=3)]

    print("Historical Anomalies:", historical_anomalies.index.tolist())
    print("Advance Alerts for Future Anomalies:", advance_alerts)


