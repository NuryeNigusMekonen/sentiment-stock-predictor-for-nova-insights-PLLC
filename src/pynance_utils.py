import pynance as pn
import pandas as pd

def calculate_pynance_metrics(df, stock_name):
    
   # Use PyNance to compute and print returns and volatility.
  #  Requires 'Adj Close' to exist.
  
    try:
        df["Daily Return"] = df["Adj Close"].pct_change()
        avg_return = df["Daily Return"].mean()
        volatility = df["Daily Return"].std()
        annual_return = avg_return * 252
        annual_volatility = volatility * (252 ** 0.5)

        print(f" PyNance Metrics for {stock_name}:")
        print(f"  - Daily Mean Return    : {avg_return:.5f}")
        print(f"  - Daily Volatility     : {volatility:.5f}")
        print(f"  - Annualized Return    : {annual_return:.2%}")
        print(f"  - Annualized Volatility: {annual_volatility:.2%}")
    except Exception as e:
        print(f" PyNance failed for {stock_name}: {e}")
