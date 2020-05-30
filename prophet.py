import locale
import fbprophet
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

df = pd.read_csv('temps_2020_60day_forecast.txt', decimal='.', parse_dates=['ds'])
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=60)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
plt.show()
