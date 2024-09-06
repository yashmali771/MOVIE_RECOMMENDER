import streamlit as st
import pickle
import pandas as pd
import requests

moviesd = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(moviesd)


similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    d = similarity[movie_index]
    movie_list = sorted(list(enumerate(d)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

def fetch_poster(movie_id):
    requests.get('')

st.title("Movie Recommender System")

Selected_movie_name = st.selectbox('Type movie name',movies['title'].values)

if st.button('SHOW MOVIES'):
    recommendations = recommend(Selected_movie_name)

    for i in recommendations:
        st.write(i)