import pandas as pd

def headline_lengths(df):
    df['headline_length'] = df['headline'].apply(len)
    return df

def publisher_counts(df):
    return df['publisher'].value_counts()

def publication_trends(df):
    return df['date'].dt.date.value_counts().sort_index()

def extract_domains(df):
    df['domain'] = df['publisher'].str.extract(r'@([\w.-]+)')
    return df
