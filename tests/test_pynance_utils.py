import unittest
import pandas as pd
from src.pynance_utils import calculate_pynance_metrics

class TestPynanceUtils(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Adj Close": [100, 101, 102, 104, 103]
        })

    def test_metrics_run_without_error(self):
        try:
            calculate_pynance_metrics(self.df, "TEST")
        except Exception as e:
            self.fail(f"calculate_pynance_metrics raised an exception: {e}")

    def test_daily_return_column_created(self):
        calculate_pynance_metrics(self.df, "TEST")
        self.assertIn("Daily Return", self.df.columns)

    def test_invalid_input_handling(self):
        bad_df = pd.DataFrame({"Price": [100, 101]})  # Missing 'Adj Close'
        try:
            calculate_pynance_metrics(bad_df, "BAD")
        except Exception:
            self.fail("Exception should be caught internally by calculate_pynance_metrics")

if __name__ == "__main__":
    unittest.main()
