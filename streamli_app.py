import streamlit as st
import cv2

st.title("Webcam Test in Streamlit")

cap = cv2.VideoCapture(0, cv2.CAP_MSMF)  # Try CAP_DSHOW if MSMF fails

if not cap.isOpened():
    st.error("❌ Could not open webcam.")
else:
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame)
    else:
        st.error("❌ Failed to capture frame.")

cap.release()
