import os
import sys
import pandas as pd

# Make sure Python knows where to find src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_loader import load_news_data
from ta_indicators import add_indicators

data_dir = "Data/yfinance_data"
output_suffix = "_with_indicators.csv"

for filename in os.listdir(data_dir):
    if filename.endswith("_historical_data.csv"):
        input_path = os.path.join(data_dir, filename)
        output_path = os.path.join(data_dir, filename.replace("_historical_data.csv", output_suffix))

        try:
            df = load_news_data(input_path)
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df = add_indicators(df)
            df.to_csv(output_path, index=False)
            print(f" Processed and saved: {output_path}")
        except Exception as e:
            print(f" Failed for {filename}: {e}")
