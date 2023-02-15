import talib as ta
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


def plot_stock_graph(ticker, indicator):
    ticker_data = yf.download(ticker)
    df = pd.DataFrame(ticker_data)

    indicator_values_dict = {
        'SMA-5': ta.SMA(df['Close'], 5)
        ,
        'SMA-7': ta.SMA(df['Close'], 7)
        ,
        'SMA-9': ta.SMA(df['Close'], 9)
        ,
        'SMA-12': ta.SMA(df['Close'], 12)
        ,
        'SMA-21': ta.SMA(df['Close'], 21)
        ,
        'SMA-50': ta.SMA(df['Close'], 50)
        ,
        'SMA-100': ta.SMA(df['Close'], 100)
        ,
        'SMA-200': ta.SMA(df['Close'], 200)
        ,
        'EMA-5': ta.EMA(df['Close'], 5)
        ,
        'EMA-7': ta.EMA(df['Close'], 7)
        ,
        'EMA-9': ta.EMA(df['Close'], 9)
        ,
        'EMA-12': ta.EMA(df['Close'], 12)
        ,
        'EMA-21': ta.EMA(df['Close'], 21)
        ,
        'EMA-50': ta.EMA(df['Close'], 50)
        ,
        'EMA-100': ta.EMA(df['Close'], 100)
        ,
        'EMA-200': ta.EMA(df['Close'], 200)

    }

    ticker_data = yf.download(ticker)
    df = pd.DataFrame(ticker_data)
    df[indicator] = indicator_values_dict[indicator]
    df = df.round({'Open': 0, 'High': 0, 'Low': 0, 'Close': 0, 'SMA_100': 0})

    plt.plot(df['Close'], linewidth="1.2")
    plt.plot(indicator_values_dict[indicator], linewidth="1")

    plt.xlabel("Years")

    if ticker == "^NSEI":
        ticker = "NIFTY"

    plt.ylabel(ticker.replace('.NS', '') + " price in ₹")
    plt.title(ticker.replace('.NS', '') + ' Plotted with ' + indicator)
    plt.show()

# df['RSI'] = ta.RSI(df['Close'])
#
# fig, axs = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(10, 6))
# axs[0].plot(df['Close'])
# axs[1].axhline(y=60, color='r', linestyle='--')
# axs[1].axhline(y=40, color='g', linestyle='--')
# axs[1].plot(df['RSI'], color='orange')
