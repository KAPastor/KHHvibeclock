import streamlit as st
import requests
import json

vibe_set = ["Harshed", "Waning", "Mid", "Top Tier","Immaculate"]
vibe_values = {}
vibe_values["Harshed"] = 0
vibe_values["Waning"] = 1*180/4
vibe_values["Mid"] = 2*180/4
vibe_values["Top Tier"] = 3*180/4
vibe_values["Immaculate"] = 4*180/4

inverted_vibe_values = {value: key for key, value in vibe_values.items()}

# 🔹 Replace with your Firebase Realtime Database URL
FIREBASE_URL_SERVO = "https://vibeclock-default-rtdb.firebaseio.com/Servo.json"
FIREBASE_URL_NAME = "https://vibeclock-default-rtdb.firebaseio.com/name.json"

st.title("Kyle\'s Office Vibes")
st.subheader('Control Kyle\'s Vibe Clock!')

currentVibes =  requests.get(FIREBASE_URL_SERVO)
if inverted_vibe_values[float(currentVibes.text)] == 'Harshed':
    st.text('The Current Vibes Are')
    st.error(inverted_vibe_values[float(currentVibes.text)])

elif inverted_vibe_values[float(currentVibes.text)] == 'Immaculate':
    st.text('The Current Vibes Are')
    st.success(inverted_vibe_values[float(currentVibes.text)])
    st.balloons()
else :
    st.text('The Current Vibes Are')
    st.warning(inverted_vibe_values[float(currentVibes.text)])

currentMsg =  requests.get(FIREBASE_URL_NAME)
st.metric('Vibesetter Message',currentMsg.text)

st.divider()

st.text('When you update the vibes it will actually update the device in his office.')
# -------- POST a value --------


selected_vibe = st.selectbox(
    "Set the vibe",
    vibe_set
)

st.html("You have decided to set the vibes to:<b>" + selected_vibe + '</b>')

message= st.text_input("Send Kyle a message with your vibes", value='I am watching you...')
username= st.text_input("Let Kyle know who set the vibe", value='anonymous')

if st.button("Send the Vibes"):
    try:
        # Use PUT to overwrite the value
        response = requests.put(FIREBASE_URL_SERVO, data=json.dumps(vibe_values[selected_vibe]))
        # if response.status_code == 200:
        #     st.success(f"Value {new_value} saved successfully!")
        # else:
        #     st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Exception occurred: {e}")

    try:
        # Use PUT to overwrite the value
        messageSet = "'" + message + "' - " + username
        response = requests.put(FIREBASE_URL_NAME, data=json.dumps(messageSet))
        # if response.status_code == 200:
        #     st.success(f"Value {new_value} saved successfully!")
        # else:
        #     st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Exception occurred: {e}")

    st.success(f"Vibes have been sent.  Thanks for playing.")
    st.rerun()