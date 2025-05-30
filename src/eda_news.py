import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
from sklearn.decomposition import LatentDirichletAllocation

def headline_lengths(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['headline_length'] = df['headline'].astype(str).apply(len)
    return df

def publisher_counts(df: pd.DataFrame, top_n: int = 10) -> pd.Series:
    return df['publisher'].value_counts().head(top_n)

def publication_trends(df: pd.DataFrame) -> pd.Series:
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    return df['date'].dt.date.value_counts().sort_index()

def hourly_distribution(df: pd.DataFrame) -> pd.Series:
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        df['date'] = pd.to_datetime(df['date'])
    return df['date'].dt.hour.value_counts().sort_index()

def extract_domains(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['domain'] = df['publisher'].str.extract(r'@([\w\.-]+)')
    return df

def top_keywords(df: pd.DataFrame, top_n: int = 20) -> pd.Series:
    headlines = df["headline"].dropna().astype(str).values
    cv = CountVectorizer(stop_words="english", max_features=top_n)
    matrix = cv.fit_transform(headlines)
    keywords = pd.Series(matrix.toarray().sum(axis=0), index=cv.get_feature_names_out())
    return keywords.sort_values(ascending=False)

def generate_wordcloud(df: pd.DataFrame) -> WordCloud:
    text = " ".join(df["headline"].dropna())
    return WordCloud(width=800, height=400, background_color='white').generate(text)

def lda_topics(df: pd.DataFrame, num_topics: int = 5, num_words: int = 10) -> list:
    cv = CountVectorizer(stop_words="english")
    dtm = cv.fit_transform(df["headline"].dropna().astype(str))
    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda_model.fit(dtm)
    words = cv.get_feature_names_out()
    topics = []
    for topic in lda_model.components_:
        top_words = [words[i] for i in topic.argsort()[-num_words:][::-1]]
        topics.append(top_words)
    return topics

def extract_events(text: str) -> list:
    if not isinstance(text, str):
        return []

    patterns = [
    r'price target',
    r'fda approval',
    r'fda clearance',
    r'earnings beat',
    r'earnings miss',
    r'share buyback',
    r'acquisition',
    r'merger',
    r'dividend increase',
    r'dividend cut',
    r'downgrade',
    r'upgrade',
    r'ipo',
    r'split',
    r'layoff',
    r'guidance raise',
    r'guidance cut',
    r'guidance update'
    ]
    matches = []
    for pattern in patterns:
        found = re.findall(pattern, text.lower())
        matches.extend(found)

    return list(set(matches)) if matches else []

#Latent Dirichlet Allocation (LDA) is one of the most popular algorithms for topic modeling.
if __name__ == "__main__":
    print("Functions in eda_news.py:")
    print(dir())
