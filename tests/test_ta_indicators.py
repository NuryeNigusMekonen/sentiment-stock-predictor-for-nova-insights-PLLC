#this is also for task two
import unittest
import pandas as pd
from src.ta_indicators import add_indicators

class TestTAIndicators(unittest.TestCase):
    def test_indicators_exist(self):
        df = pd.DataFrame({
            'Close': [150, 152, 153, 151, 150, 149, 148, 150, 151, 153, 154, 152, 150, 149, 151, 153, 155, 157, 158, 160]
        })
        df = add_indicators(df)
        self.assertIn("SMA_20", df.columns)
        self.assertIn("RSI", df.columns)
        self.assertIn("MACD", df.columns)

if __name__ == '__main__':
    unittest.main()
