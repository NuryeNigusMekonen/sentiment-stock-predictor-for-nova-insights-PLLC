import talib

def add_technical_indicators(df):
    try:
        df["MA20"] = talib.SMA(df["Adj Close"], timeperiod=20)
        df["RSI"] = talib.RSI(df["Adj Close"], timeperiod=14)
        macd, macdsignal, _ = talib.MACD(df["Adj Close"])
        df["MACD"] = macd
        df["MACD_Signal"] = macdsignal
    except Exception as e:
        raise RuntimeError(f"Failed to compute indicators: {e}")
    return df
