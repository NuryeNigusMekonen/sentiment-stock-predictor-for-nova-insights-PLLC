#this is optional as i am a trader i want to further test the 
# if it possible to generate buy and sell signal 
# so that i will test it in real world data
def generate_signals(df):
   
    ##Generate buy and sell signals using:
    #- Buy: RSI < 30 and MACD crosses above signal
    #- Sell: RSI > 70 and MACD crosses below signal
    
    required = {"RSI", "MACD", "MACD_Signal", "Adj Close"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required - set(df.columns)}")

    # MACD crossovers
    df["MACD_Cross_Up"] = (df["MACD"] > df["MACD_Signal"]) & (df["MACD"].shift(1) < df["MACD_Signal"].shift(1))
    df["MACD_Cross_Down"] = (df["MACD"] < df["MACD_Signal"]) & (df["MACD"].shift(1) > df["MACD_Signal"].shift(1))

    # Buy: Oversold + bullish crossover
    df["Buy_Signal"] = (df["RSI"] < 30) & df["MACD_Cross_Up"]

    # Sell: Overbought + bearish crossover
    df["Sell_Signal"] = (df["RSI"] > 70) & df["MACD_Cross_Down"]

    return df
