import streamlit as st
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, we are Tech Titans :wave:")
    st.title("Heart disease detection")
    st.write(
        "To detect cardiac diseases"
    )
    age1=st.number_input('Enter AGE in Years : ',min_value=0)
    age1*=365
    gender1=st.number_input('Enter 1 for MALE and 2 for FEMALE : ',min_value=0)
    height1=st.number_input('Enter Height in cm : ',min_value=0)
    weight1=st.number_input('Enter weight in kg : ',min_value=0)
    hibp1=st.number_input('Enter the High Action Pulse (AP) : ',min_value=0)
    lwbp1=st.number_input('Enter the Low Action Pulse (AP) : ',min_value=0)
    chl1=st.number_input('Enter Cholesterol 1/2/3 : ',min_value=0)
    glu1=st.number_input('Enter Glucose 1/2/3 : ',min_value=0)
    smo1=st.number_input('Do you Smoke? 0/1 : ',min_value=0)
    alco1=st.number_input('Do you consume Alcohol? 0/1: ',min_value=0)
    car1=st.number_input('Doing Cardio? 0/1 : ',min_value=0)