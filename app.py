import streamlit as st

st.title("ML From Scratch 🚀")

st.write("Welcome to ML From Scratch Project")

algo = st.sidebar.selectbox(
    "Choose Algorithm",
    [
        "Linear Regression",
        "KNN",
        "K-Means",
        "Logistic Regression",
        "Decision Tree",
        "Naive Bayes",
        "Perceptron"
    ]
)

st.success(f"You selected: {algo}")

st.write("More algorithms coming soon 🔥")

# if algo == "Linear Regression":
#     from pages.linear_page import run
#     run()

# elif algo == "KNN":
#     from pages.knn_page import run
#     run()