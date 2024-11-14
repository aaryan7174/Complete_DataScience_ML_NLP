import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name=st.text_input("Enter your Name")
age= st.slider("Select Your Age : ", 1,100,25)
st.write(f"Your Age is {age}")
if name:
   st.write(f"Hello, {name}") 
   
options = ["Python","Java","C++","JavaScript"]
choice= st.selectbox("Choose your favourite Language:", options)
st.write(f"You selected {choice}")


data={
    "Name" : ["Aaryan","Anil","Jake","John"],
    "Age"  : [28,24,35,40],
    "City" : ["New York","New York","Chicago","Houston"]
}
df=pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)