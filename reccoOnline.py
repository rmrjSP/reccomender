import streamlit as st

st.write("Recommendations")

# %%

import pandas as pd

# %%
books_df = pd.read_csv('books.csv')
animanga_df = pd.read_csv('data.csv')
movies_df = pd.read_csv('imdb_top_1000.csv')

# %%
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# %%
books_df = books_df[['title', 'description', 'categories']]
animanga_df = animanga_df[['title', 'description', 'tags']]
movies_df = movies_df[['Series_Title', 'Overview', 'Genre']]

# %%
import re

def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", title)

# %%
books_df['description'] = books_df['description'].astype(str)
books_df['categories'] = books_df['categories'].astype(str)
animanga_df['description'] = animanga_df['description'].astype(str)
animanga_df['title'] = animanga_df['title'].astype(str)
animanga_df['tags'] = animanga_df['tags'].astype(str)

# %%
movies_df['Series_Title'] = movies_df['Series_Title'].apply(clean_title)
movies_df['Overview'] = movies_df['Overview'].apply(clean_title)
movies_df['Genre'] = movies_df['Genre'].apply(clean_title)
animanga_df['title'] = animanga_df['title'].apply(clean_title)
animanga_df['description'] = animanga_df['description'].apply(clean_title)
animanga_df['tags'] = animanga_df['tags'].apply(clean_title)
books_df['title'] = books_df['title'].apply(clean_title)
books_df['description'] = books_df['description'].apply(clean_title)
books_df['categories'] = books_df['categories'].apply(clean_title)

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ngram_range=(1,2))
#tfidf = vectorizer.fit_transform(movies_df['Overview'])
#tfidfT = vectorizer.fit_transform(movies_df['Series_Title'])
#tfidfG = vectorizer.fit_transform(movies_df['Genre'])
#Use one of these, only the one you need on the thingy down there idk which, which everone is there will work


# %%
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
 
def searchMT(title):
   
    title = clean_title(title)
    tfidfT = vectorizer.fit_transform(movies_df['Series_Title'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfT).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies_df.iloc[indices]
    return results
def searchMD(title):
   
    title = clean_title(title)
    tfidfT = vectorizer.fit_transform(movies_df['Overview'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfT).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies_df.iloc[indices]
    return results
def searchMC(title):
   
    title = clean_title(title)
    tfidfT = vectorizer.fit_transform(movies_df['Genre'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfT).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies_df.iloc[indices]
    return results



# %%
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
 
def searchBT(title):
   
    title = clean_title(title)
    tfidfB = vectorizer.fit_transform(books_df['title'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfB).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = books_df.iloc[indices]
    return results
def searchBD(title):
   
    title = clean_title(title)
    tfidfB = vectorizer.fit_transform(books_df['description'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfB).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = books_df.iloc[indices]
    return results
def searchBC(title):
   
    title = clean_title(title)
    tfidfB = vectorizer.fit_transform(books_df['categories'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfB).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = books_df.iloc[indices]
    return results

# %%
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
 
def searchAT(title):
   
    title = clean_title(title)
    tfidfA = vectorizer.fit_transform(animanga_df['title'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfA).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = animanga_df.iloc[indices]
    return results
def searchAD(title):
   
    title = clean_title(title)
    tfidfA = vectorizer.fit_transform(animanga_df['description'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfA).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = animanga_df.iloc[indices]
    return results
def searchAC(title):
   
    title = clean_title(title)
    tfidfA = vectorizer.fit_transform(animanga_df['tags'])
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidfA).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = animanga_df.iloc[indices]
    return results

# %%
option = st.selectbox(
    'How would you like to search?',
    ('title', 'description', 'tags'))
user_input = st.text_input("Title", "harry potter")
if option == 'title': 
    st.write("Similar Books")
    st.dataframe(searchBT(user_input))
    st.write("Similar Movies")
    st.dataframe(searchMT(user_input))
    st.write("Similar Animanga")
    st.dataframe(searchAT(user_input))
if option == 'description':
    st.write("Similar Books")
    st.dataframe(searchBD(user_input))
    st.write("Similar Movies")
    st.dataframe(searchMD(user_input))
    st.write("Similar Animanga")
    st.dataframe(searchAD(user_input))
if option == 'tags':
    st.write("Similar Books")
    st.dataframe(searchBC(user_input))
    st.write("Similar Movies")
    st.dataframe(searchMC(user_input))
    st.write("Similar Animanga")
    st.dataframe(searchAC(user_input))