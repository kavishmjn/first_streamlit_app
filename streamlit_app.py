import streamlit
import pandas as pd
streamlit.title('mom\'s new diner'.upper())
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits-fruits.set_index('Fruit')
#selecting fruit
streamlit.multiselect("Pick some fruits: ", list(fruits.index))
streamlit.dataframe(fruits)
