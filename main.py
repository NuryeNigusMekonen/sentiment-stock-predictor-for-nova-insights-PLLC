# main.py

import os
from src.data_loader import load_news_data, load_stock_data

from src.eda_news import (
    extract_events,
    lda_topics,
    publication_trends,
    top_keywords,
    extract_domains
)
from src.ta_indicators import add_technical_indicators
from src.pynance_utils import calculate_pynance_metrics
from src.generate_signals import generate_signals
from src.visualizer import plot_trade_signals, plot_indicators

def main():
    print(" Starting Nova Insights Sentiment-Stock Predictor Pipeline...\n")

    # Step 1: Load Financial News
    news_path = "Data/raw_analyst_ratings.csv"
    print(f" Loading news data from: {news_path}")
    news_df = load_news_data(news_path)

    # Step 2: News EDA & Sentiment Extraction 
    print(" Extracting sentiment scores from headlines...")
    news_df = extract_events(news_df)

    print("\n Top Keywords:")
    keywords = top_keywords(news_df)
    print(keywords)

    print("\n Publication Trends by Date:")
    trends = publication_trends(news_df)
    print(trends.tail())

    print("\n LDA Topic Modeling Results:")
    topics = lda_topics(news_df, num_topics=5)
    for i, topic in enumerate(topics):
        print(f"  Topic {i+1}: {', '.join(topic)}")

    print("\n Extracting Publisher Domains:")
    news_df = extract_domains(news_df)
    print(news_df["domain"].value_counts().head())

    # Step 3: Load Historical Stock Data
    stock_dir = "data/yfinance_data/"
    print(f"\n Loading stock price data from: {stock_dir}")
    stock_data = load_stock_data(stock_dir)

    # Step 4: Process Each Stock File 
    for ticker, df in stock_data.items():
        print(f"\n Processing stock: {ticker}")

        # Add technical indicators
        df = add_technical_indicators(df)

        # Calculate performance metrics
        calculate_pynance_metrics(df, stock_name=ticker)

        # Generate buy/sell signals
        df = generate_signals(df)

        # Visualize results
        print(f" Visualizing signals for {ticker}")
        plot_trade_signals(df, stock_name=ticker)
        plot_indicators(df, stock_name=ticker)

    print("\n Pipeline completed successfully.")

if __name__ == "__main__":
    main()
