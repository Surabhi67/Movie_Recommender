import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)


    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZDA3YzQwZmFkNDllNWNmMzQ3MjhmY2MxNzk2OWJmNSIsInN1YiI6IjY1ZTYxMGYzZmUwNzdhMDE2MjEwN2M5NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lrYKK0da7Sl0OP0DAItfyJHJSkJsM5gaQV7oXleGZ2Y"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    


movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[movie_index]),reverse=True,key=lambda x:x[1])[1:6]
    recommended = []
    poster = []
    for i in distances:
        movie_id = movies.iloc[i[0]].movie_id
        recommended.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_id))
    return recommended, poster

st.title("Movie Recommender System")

similarity = pickle.load(open('similarity.pkl','rb'))

option = st.selectbox(
    'Movie Name',
    movies_list, 
    index = None,
    placeholder = "Choose your movie",)

if st.button("Recommend"):
    names, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

