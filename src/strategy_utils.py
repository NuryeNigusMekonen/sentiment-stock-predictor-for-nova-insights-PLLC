import pandas as pd

def merge_sentiment_all_stocks(news_df, stock_data):
    """
    Merge sentiment scores with price data for all tickers by date.
    
    Parameters:
    - news_df: DataFrame with 'ticker', 'date', and 'polarity'
    - stock_data: dict of {ticker: DataFrame with 'Date' column}
    
    Returns:
    - dict of {ticker: merged DataFrame with avg_sentiment}
    """
    news_df = news_df.copy()

    # Normalize datetime: remove timezone and time info
    news_df["date"] = pd.to_datetime(news_df["date"], errors="coerce").dt.tz_localize(None).dt.normalize()

    # Drop any rows where date couldn't be parsed
    news_df = news_df.dropna(subset=["date"])

    # Group sentiment by ticker + date
    sentiment = (
        news_df.groupby(["ticker", "date"])["polarity"]
        .mean()
        .reset_index()
        .rename(columns={"polarity": "avg_sentiment"})
    )

    merged_data = {}

    for ticker, price_df in stock_data.items():
        if ticker not in sentiment["ticker"].unique():
            print(f" Skipping {ticker}: No sentiment data available.")
            continue

        # Filter sentiment data for current ticker
        s_df = sentiment[sentiment["ticker"] == ticker].copy()

        # Prepare stock price data
        df = price_df.copy().reset_index()  # Assuming 'Date' is index
        df["date"] = pd.to_datetime(df["Date"], errors="coerce").dt.normalize()

        # Merge on normalized date
        merged = pd.merge(df, s_df, on="date", how="left")

        # Restore original Date index
        merged.set_index("Date", inplace=True)

        merged_data[ticker] = merged

    return merged_data
