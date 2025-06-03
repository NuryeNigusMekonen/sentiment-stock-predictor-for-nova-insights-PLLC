import unittest
import pandas as pd
from textblob import TextBlob
import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(".."))

from src.nlp_utils import extract_sentiment 

class TestExtractSentiment(unittest.TestCase):
    def test_polarity_column_added(self):
        # Sample data
        data = {
            "headline": [
                "I love this product!",
                "This is terrible.",
                "It's okay, not great.",
                ""
            ]
        }
        df = pd.DataFrame(data)
        
        # Run function
        result_df = extract_sentiment(df)
        
        # Check if polarity column is added
        self.assertIn("polarity", result_df.columns)
        
        # Check polarity values are floats within range [-1, 1]
        for val in result_df["polarity"]:
            self.assertIsInstance(val, float)
            self.assertGreaterEqual(val, -1.0)
            self.assertLessEqual(val, 1.0)

    def test_empty_headline(self):
        df = pd.DataFrame({"headline": [""]})
        result_df = extract_sentiment(df)
        self.assertIn("polarity", result_df.columns)
        # Empty string polarity should be 0
        self.assertEqual(result_df["polarity"].iloc[0], 0.0)

if __name__ == "__main__":
    unittest.main()
