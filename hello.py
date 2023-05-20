# simple app to test streamlit

import streamlit as st

st.title("hello word")
st.header("this is a header")
st.subheader(" this is subheader : http://www.equipement.gov.ma")

st.write("simple test for streamlit")

if st.button("click me"):
    st.write("you clicked me!")
    st.balloons()


st.sidebar.header("this is sidebar")
button = st.sidebar.button(label = "cliquez ici")
if button:
    st.sidebar.write("bonjour")
    st.write("test")
    st.sidebar.balloons()

# create columns first with 2/3

button2 = st.button(label = "cliquez pour afficher")
col1, col2 = st.columns([2,1])

if button2:
    col1.header("c'est la colonne 1")
    col1.write("colonne 1")
    col2.header("c'est la colonne 2")
    col2.write("colonne 2")

option = st.selectbox( 'comment vous voulez être contacté', ('Email', 'tel', 'mobile'))

st.write ('vous avez sélectionné :', option)
