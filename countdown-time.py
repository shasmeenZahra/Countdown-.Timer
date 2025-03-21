import time
import streamlit as st

# Streamlit UI Setup
st.set_page_config(page_title="Countdown Timer", layout="centered")
st.title("⏳ Advanced Countdown Timer")

# User input for time entry
seconds = st.number_input("Enter time (seconds):", min_value=1, step=1, value=10)

# Timer display
timer_placeholder = st.empty()

# Control buttons
start = st.button("Start")
pause = st.button("Pause")
resume = st.button("Resume")
reset = st.button("Reset")

# Timer logic
if "running" not in st.session_state:
    st.session_state.running = False
if "time_left" not in st.session_state:
    st.session_state.time_left = seconds

if start:
    st.session_state.running = True
    st.session_state.time_left = seconds

if pause:
    st.session_state.running = False

if resume:
    st.session_state.running = True

if reset:
    st.session_state.running = False
    st.session_state.time_left = seconds

def countdown():
    while st.session_state.time_left > 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.time_left, 60)
        timer_placeholder.markdown(f"## {mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state.time_left -= 1
    if st.session_state.time_left == 0 and st.session_state.running:
        timer_placeholder.markdown("## 🎉 Time's Up!")
        st.session_state.running = False

# Start countdown in the Streamlit loop
if st.session_state.running:
    countdown()
