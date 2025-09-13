# data_utils.py

import pandas as pd

def load_data(filepath="metadata.csv"):
    df = pd.read_csv(filepath, low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna("No abstract")
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

def filter_by_year(df, start_year, end_year):
    return df[df['year'].between(start_year, end_year)]
