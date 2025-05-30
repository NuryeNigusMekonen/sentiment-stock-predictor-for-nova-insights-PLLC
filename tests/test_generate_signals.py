import unittest
from src.generate_signals import generate_signals  # assuming this function exists
import pandas as pd

class TestGenerateSignals(unittest.TestCase):
    
    def test_signal_logic(self):
        df = pd.DataFrame({
            "Close": [100, 102, 105, 103, 101],
            "SMA20": [100, 101, 102, 102, 100],
            "Adj Close": [100, 102, 105, 103, 101],
            "RSI": [50, 60, 70, 65, 60],
            "MACD": [0.2, 0.4, 0.6, 0.5, 0.3],
            "MACD_Signal": [0.1, 0.3, 0.5, 0.6, 0.4]
        })

        from src.generate_signals import generate_signals
        result = generate_signals(df)

        self.assertIn("Buy_Signal", result.columns)
        self.assertIn("Sell_Signal", result.columns)
        self.assertIn("MACD_Cross_Up", result.columns)
        self.assertIn("MACD_Cross_Down", result.columns)
        #self.assertTrue(result["Buy_Signal"].any() or result["Sell_Signal"].any())


if __name__ == '__main__':
    unittest.main()
