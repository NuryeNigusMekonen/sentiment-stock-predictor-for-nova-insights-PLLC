import unittest
import pandas as pd
from eda_news import headline_lengths, publisher_counts, publication_trends, extract_domains

class TestEDANews(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'headline': ["Stock soars", "Market dips", "Apple earnings beat"],
            'publisher': ["news@marketwatch.com", "news@bloomberg.com", "info@investor.com"],
            'date': pd.to_datetime(["2024-05-01", "2024-05-01", "2024-05-02"])
        })

    def test_headline_lengths(self):
        df_out = headline_lengths(self.df)
        self.assertIn('headline_length', df_out.columns)

    def test_publisher_counts(self):
        counts = publisher_counts(self.df)
        self.assertTrue('news@marketwatch.com' in counts.index)

    def test_publication_trends(self):
        trends = publication_trends(self.df)
        self.assertEqual(len(trends), 2)  # Two unique dates

    def test_extract_domains(self):
        df_out = extract_domains(self.df)
        self.assertIn('domain', df_out.columns)
        self.assertEqual(df_out.loc[0, 'domain'], 'marketwatch.com')

if __name__ == '__main__':
    unittest.main()
