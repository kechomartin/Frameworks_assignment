# app.py

import streamlit as st
from data_utils import load_data, filter_by_year
from visuals import plot_publications_per_year, plot_top_journals, generate_wordcloud

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata")

df = load_data()
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered_df = filter_by_year(df, year_range[0], year_range[1])

st.subheader("Publications per Year")
st.pyplot(plot_publications_per_year(filtered_df))

st.subheader("Top Journals")
st.pyplot(plot_top_journals(filtered_df))

st.subheader("Word Cloud of Titles")
st.pyplot(generate_wordcloud(filtered_df))

st.subheader("Sample Data")
st.dataframe(filtered_df.head())
