import pandas as pd
import os

def load_stock_files(folder_path: str) -> dict:
    """
    Loads all stock CSV files from a folder into a dictionary.
    Reuses the `load_stock_data()` function for consistency.
    """
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Directory not found: {folder_path}")

    stock_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            ticker = filename.split("_")[0]  # assumes filenames like AAPL_historical_data.csv
            full_path = os.path.join(folder_path, filename)
            try:
                df = load_stock_data(full_path)  #  Reuse your validated single loader
                stock_data[ticker] = df
            except Exception as e:
                print(f" Skipped {filename}: {e}")

    if not stock_data:
        raise ValueError("No valid stock files loaded.")

    return stock_data

def load_news_data(news_path: str) -> pd.DataFrame:
    if not os.path.exists(news_path):
        raise FileNotFoundError(f"News file not found: {news_path}")
    try:
        df = pd.read_csv(news_path)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load news file: {e}")
    
    return df
def load_stock_data(filepath): #used to import single csv file 
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
def load_filtered_news(tickers, folder="../Data/filtered/"):
    all_news = []
    for t in tickers:
        path = os.path.join(folder, f"{t}_filtered_news.csv")
        if os.path.exists(path):
            df = pd.read_csv(path)
            df["ticker"] = t  # for consistency
            all_news.append(df)
        else:
            print(f" Missing file: {path}")
    return pd.concat(all_news, ignore_index=True)
