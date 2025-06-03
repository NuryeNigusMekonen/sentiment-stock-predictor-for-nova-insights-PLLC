import pandas as pd

def merge_sentiment_all_stocks(news_df: pd.DataFrame, stock_data: dict) -> dict:
    news_df = news_df.copy()
    #  Robust parsing of mixed-format datetime strings
    news_df["date"] = pd.to_datetime(news_df["date"], errors="coerce").dt.date
    news_df.dropna(subset=["date"], inplace=True)
    #  Aggregate daily average sentiment
    daily_sentiment = news_df.groupby("date")["polarity"].mean().reset_index()
    daily_sentiment.rename(columns={"polarity": "avg_sentiment"}, inplace=True)
    merged_data = {}
    for ticker, df in stock_data.items():
        df = df.copy()
        # Extract date from datetime index or column
        if "Date" in df.columns:
            df["date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date
        elif df.index.name == "Date":
            df["date"] = df.index.date
        else:
            raise ValueError(f"Date column not found in stock data for {ticker}")
        #  Merge average sentiment
        merged_df = pd.merge(df, daily_sentiment, on="date", how="left")
        merged_data[ticker] = merged_df
    return merged_data
