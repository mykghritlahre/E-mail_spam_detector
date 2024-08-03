import streamlit as st
from spam_detector import predict_spam

st.title("Spam Detector")

email_input = st.text_area("Enter your email here:")

if st.button("Predict"):
    result = predict_spam(email_input)
    st.write(f"The email is: {result}")