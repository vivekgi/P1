import streamlit as st
import requests

# Define the API endpoint URL
api_endpoint = "https://example.com/api/endpoint"  # Replace with your API endpoint URL

# Function to make the API request and print the status
def invoke_endpoint():
    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            st.success(f"API call successful! Status Code: {response.status_code}")
        else:
            st.error(f"API call failed! Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app
st.title("Invoke API Endpoint and Print Status")

# Create a button to invoke the API endpoint
if st.button("Invoke API Endpoint"):
    invoke_endpoint()
