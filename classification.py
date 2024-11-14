import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names, iris.feature_names

# Load data, target names, and feature names
df, target_names, feature_names = load_data()

# Initialize and train the model
model = RandomForestClassifier()
model.fit(df[feature_names], df['species'])

# Sidebar inputs
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Prepare input data for prediction
input_data = [sepal_length, sepal_width, petal_length, petal_width]

# Prediction
prediction = model.predict([input_data])
predicted_species = target_names[prediction[0]]

# Display prediction result
st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")
