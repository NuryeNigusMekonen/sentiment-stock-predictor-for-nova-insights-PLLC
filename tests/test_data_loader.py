import unittest
from src.data_loader import load_news_data, load_stock_data
import os

class TestDataLoader(unittest.TestCase):

    def test_news_path_error(self):
        with self.assertRaises(FileNotFoundError):
            load_news_data("Data/does_not_exist.csv")

    def test_stock_folder_error(self):
        with self.assertRaises(FileNotFoundError):
            load_stock_data("Data/missing_folder")

if __name__ == '__main__':
    unittest.main()
