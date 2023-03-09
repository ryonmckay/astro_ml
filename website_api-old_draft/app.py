import streamlit as st
import requests
import datetime

# Define the URL for your prediction API
prediction_api_url = "http://your-prediction-api-url.com/predict"

# Define the web app using Streamlit
st.title("Birth Prediction App")
st.write("Enter your birth details below to get your prediction!")

with st.form(key='prediction_form'):
    # Create input fields for the user's birth details
    birth_date = st.date_input("Birth date")
    birth_time = st.time_input("Birth time")
    birth_place = st.text_input("Birth place")
    submit_button = st.form_submit_button(label="Get Prediction")

# When the user clicks the "Get Prediction" button, send a request to the prediction API
if submit_button:
    # Convert the birth date and time into a datetime object
    birth_datetime = datetime.datetime.combine(birth_date, birth_time)

    # Prepare the data to send to the API
    data = {
        "birth_datetime": birth_datetime.isoformat(),
        "birth_place": birth_place
    }

    # Send a POST request to the prediction API with the user's birth details
    response = requests.post(prediction_api_url, json=data)

    # If the request was successful, display the prediction to the user
    if response.ok:
        prediction = response.json()["prediction"]
        st.write(f"Your prediction is: {prediction}")
    else:
        st.write("Error: Failed to get prediction from API")
