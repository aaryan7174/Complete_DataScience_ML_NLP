import streamlit as st
import pandas as pd
import numpy as np

# Title of Application 

st.title("Hello Streamlit")

# Display a simple text
st.write("This is a simple text")

# Create a simple dataframe
df= pd.DataFrame({
    "First Column" : [1,2,3,4],
    "Second Column": [10, 20, 30, 40]
})

st.write("Here is a Dataframe")
st.write(df)

# Create a line chart 
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)