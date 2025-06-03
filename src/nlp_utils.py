from textblob import TextBlob
import pandas as pd

def extract_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a 'polarity' score to each headline using TextBlob.
    Polarity ranges from -1 (negative) to +1 (positive).
    """
    df = df.copy()
    df["polarity"] = df["headline"].astype(str).apply(lambda x: TextBlob(x).sentiment.polarity)
    return df
