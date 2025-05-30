import unittest
import pandas as pd
from src.eda_news import (
    headline_lengths, publisher_counts, publication_trends,
    hourly_distribution, extract_domains, top_keywords,
    lda_topics, extract_events
)

class TestEDANews(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "headline": ["FDA approval granted", "price target raised", "earnings beat expected"],
            "publisher": ["news@example.com", "finance@corp.org", "market@invest.com"],
            "date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-02"])
        })

    def test_headline_lengths(self):
        df = headline_lengths(self.df)
        self.assertIn("headline_length", df.columns)

    def test_publisher_counts(self):
        counts = publisher_counts(self.df)
        self.assertTrue(len(counts) > 0)

    def test_publication_trends(self):
        trends = publication_trends(self.df)
        self.assertEqual(len(trends), 2)

    def test_extract_events(self):
        events = extract_events("Company announces price target and FDA approval")
        self.assertIn("price target", events)
        self.assertIn("fda approval", events)

if __name__ == '__main__':
    unittest.main()
