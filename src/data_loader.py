import pandas as pd
import os

def load_news_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_csv(filepath)
    
    # Ensure the 'date' column is parsed as datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')  # handles invalid formats too
    else:
        raise KeyError("Expected 'date' column not found in file")
    
    return df
def load_stock_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        df = pd.read_csv(filepath, parse_dates=["Date"])
    except Exception as e:
        raise ValueError(f"Failed to load CSV: {e}")

    required_cols = {"Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Missing columns: {required_cols - set(df.columns)}")

    df.sort_values("Date", inplace=True)
    df.set_index("Date", inplace=True)
    df.drop(columns=["Dividends", "Stock Splits"], inplace=True, errors="ignore")

    return df