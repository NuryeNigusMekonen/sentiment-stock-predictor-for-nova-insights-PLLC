import unittest
from src.visualizer import plot_trade_signals, plot_indicators
import pandas as pd
class TestVisualizer(unittest.TestCase):


    def setUp(self):
        self.df = pd.DataFrame({
            "Adj Close": [100, 101, 102, 103, 102],
            "Buy_Signal": [False, True, False, False, False],
            "Sell_Signal": [False, False, False, True, False],
            "MA20": [100, 101, 102, 102, 101],
            "RSI": [45, 55, 65, 75, 60],
            "MACD": [0.5, 0.6, 0.4, 0.2, 0.1],
            "MACD_Signal": [0.4, 0.5, 0.3, 0.25, 0.15]
        })
        self.df.index = pd.date_range("2023-01-01", periods=5)

    def test_plot_signals_runs(self):
        try:
            plot_trade_signals(self.df.copy(), "TEST")
        except Exception as e:
            self.fail(f"plot_trade_signals raised an error: {e}")

    def test_plot_indicators_runs(self):
        try:
            plot_indicators(self.df.copy(), "TEST")
        except Exception as e:
            self.fail(f"plot_indicators raised an error: {e}")

if __name__ == "__main__":
    unittest.main()
