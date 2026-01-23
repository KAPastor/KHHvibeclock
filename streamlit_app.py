import streamlit as st
import requests
import json

# 🔹 Replace with your Firebase Realtime Database URL
FIREBASE_URL = "https://vibeclock-default-rtdb.firebaseio.com/Servo.json"

st.title("Firebase GET & POST Demo")

# -------- POST a value --------
st.subheader("POST a value")
new_value = st.number_input("Enter a number to save", value=90, step=1)

if st.button("Save to Firebase"):
    try:
        # Use PUT to overwrite the value
        response = requests.put(FIREBASE_URL, data=json.dumps(new_value))
        if response.status_code == 200:
            st.success(f"Value {new_value} saved successfully!")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Exception occurred: {e}")

# -------- GET the value --------
st.subheader("GET the value")
if st.button("Retrieve value from Firebase"):
    try:
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200:
            data = response.json()
            if data is None:
                st.warning("No value found in Firebase yet!")
            else:
                st.info(f"Current value: {data}")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Exception occurred: {e}")
