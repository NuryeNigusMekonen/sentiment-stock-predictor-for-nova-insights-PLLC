import unittest
import pandas as pd
from src.ta_indicators import add_technical_indicators

class TestTAIndicators(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Adj Close": [100 + i for i in range(50)]  # at least 30-50 for MA/MACD
        })

    def test_indicators_added(self):
        result = add_technical_indicators(self.df.copy())
        for col in ["MA20", "RSI", "MACD", "MACD_Signal"]:
            self.assertIn(col, result.columns)

    def test_invalid_data_handling(self):
        bad_df = pd.DataFrame({"Close": [100, 102]})  # Missing 'Adj Close'
        with self.assertRaises(RuntimeError):
            add_technical_indicators(bad_df)

if __name__ == "__main__":
    unittest.main()
