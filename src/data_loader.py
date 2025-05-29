import pandas as pd
import os

def load_news_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_csv(filepath)
    
    # Ensure the 'date' column is parsed as datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')  # handles invalid formats too
    else:
        raise KeyError("Expected 'date' column not found in file")
    
    return df
