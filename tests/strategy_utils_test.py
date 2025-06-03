import unittest
import pandas as pd
from datetime import datetime
import os
import sys
import warnings  # Add this to suppress warnings

sys.path.append(os.path.abspath(".."))
from src.strategy_utils import merge_sentiment_all_stocks  # Replace with your actual module name

class TestMergeSentimentAllStocks(unittest.TestCase):

    def setUp(self):
        self.news_data = pd.DataFrame({
            "date": ["2025-05-28", "2025-05-29", "2025-05-29", "2025-05-30"],
            "polarity": [0.1, -0.2, 0.3, 0.0]
        })

        self.stock_data = {
            "AAPL": pd.DataFrame({
                "Date": pd.to_datetime(["2025-05-28", "2025-05-29", "2025-05-30"]),
                "Close": [150, 152, 155]
            }),
            "MSFT": pd.DataFrame({
                "Date": pd.to_datetime(["2025-05-28", "2025-05-29", "2025-05-30"]),
                "Close": [250, 255, 260]
            }),
        }

    def test_merge_basic(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            merged = merge_sentiment_all_stocks(self.news_data, self.stock_data)

        self.assertSetEqual(set(merged.keys()), set(self.stock_data.keys()))
        for ticker, df in merged.items():
            self.assertIn("avg_sentiment", df.columns)
            self.assertIn("date", df.columns)
            row = df[df["date"] == datetime.strptime("2025-05-29", "%Y-%m-%d").date()]
            self.assertAlmostEqual(row["avg_sentiment"].values[0], 0.05)

    def test_date_parsing_error(self):
        bad_stock_data = {
            "BAD": pd.DataFrame({"Close": [100, 101, 102]})
        }
        with self.assertRaises(ValueError):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                merge_sentiment_all_stocks(self.news_data, bad_stock_data)

    def test_news_date_coercion(self):
        news_bad_dates = self.news_data.copy()
        news_bad_dates.loc[0, "date"] = "not-a-date"
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            merged = merge_sentiment_all_stocks(news_bad_dates, self.stock_data)

        for df in merged.values():
            self.assertIn("avg_sentiment", df.columns)

if __name__ == "__main__":
    unittest.main()
