import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
import numpy as np
from src.decomposition import decompose_time_series

class TestDecomposeTimeSeries(unittest.TestCase):

    def test_decompose_time_series(self):
        dates = pd.date_range(start='2023-01-01', periods=60, freq='D')
        data = pd.Series(10 + 0.1 * np.arange(60), index=dates)
        df = pd.DataFrame({'Close': data})

        # Run decomposition with plot=False to avoid GUI issues
        result_df = decompose_time_series(df, column='Close', period=7, model='additive', plot=False)

        self.assertIn('Close_trend', result_df.columns)
        self.assertIn('Close_seasonal', result_df.columns)
        self.assertIn('Close_residual', result_df.columns)
        self.assertEqual(len(result_df), len(df))
        self.assertGreater(result_df['Close_trend'].notna().sum(), 0)
        self.assertGreater(result_df['Close_seasonal'].notna().sum(), 0)
        self.assertGreater(result_df['Close_residual'].notna().sum(), 0)

if __name__ == '__main__':
    unittest.main()
