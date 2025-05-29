from src.data_loader import load_news_data
from src.eda_news import headline_lengths, publisher_counts, publication_trends, extract_domains

file_path = "Data/yfinance_data/raw_analyst_ratings.csv"

try:
    df = load_news_data(file_path)
    df = headline_lengths(df)
    pub_counts = publisher_counts(df)
    pub_trends = publication_trends(df)
    df = extract_domains(df)

    print("Top Publishers:\n", pub_counts.head())
    print("Publication Trends:\n", pub_trends.head())

except Exception as e:
    print(f"Error: {e}")
