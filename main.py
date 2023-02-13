import talib as ta
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

ticker = 'RELIANCE.NS'
start_date = '2022-8-11'
end_date = '2023-2-13'
data_source = 'yahoo'

ticker_data = yf.download(ticker)

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.DataFrame(ticker_data)
df['EMA_100'] = ta.EMA(df['Close'], 100)
df = df.round({'Open': 0, 'High': 0, 'Low': 0, 'Close': 0, 'SMA_100': 0})
print(df)

df['LinearReg'] = ta.LINEARREG(df['Close'], 100)
plt.plot(df['Close'])
# plt.plot(df['EMA_100'])
plt.plot(df['LinearReg'])

# df['RSI'] = ta.RSI(df['Close'])
#
# fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(10, 6))
# axs[0].plot(df['Close'])
# axs[1].axhline(y=60, color='r', linestyle='--')
# axs[1].axhline(y=40, color='g', linestyle='--')
# axs[1].plot(df['RSI'], color='orange')
plt.show()
