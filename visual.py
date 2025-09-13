# visuals.py

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter

def plot_publications_per_year(df):
    papers_per_year = df['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    papers_per_year.plot(kind='bar', ax=ax)
    ax.set_title("Publications per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Count")
    return fig

def plot_top_journals(df, top_n=10):
    top_journals = df['journal'].value_counts().head(top_n)
    fig, ax = plt.subplots()
    top_journals.plot(kind='barh', ax=ax)
    ax.set_title("Top Journals")
    ax.set_xlabel("Number of Papers")
    return fig

def generate_wordcloud(df):
    titles = df['title'].dropna().apply(lambda x: re.findall(r'\b\w+\b', x.lower()))
    word_freq = Counter([word for sublist in titles for word in sublist if len(word) > 3])
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(word_freq)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    return fig
