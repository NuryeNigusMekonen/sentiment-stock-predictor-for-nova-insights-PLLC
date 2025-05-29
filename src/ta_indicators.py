#this is for task two
import talib
import pandas as pd

def add_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], _, _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df
