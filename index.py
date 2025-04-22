import time
import streamlit as st

# Page Config
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 10
if "input_time" not in st.session_state:
    st.session_state.input_time = 10

# Countdown Timer Function
def countdown_timer():
    st.session_state.remaining_time = st.session_state.input_time
    st.session_state.running = True
    placeholder = st.empty()

    while st.session_state.remaining_time >= 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        with placeholder.container():
            st.markdown(f"""
                <div style='
                    text-align: center;
                    font-size: 48px;
                    font-weight: bold;
                    color: #ffffff;
                    background-color: #4caf50;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);'>
                    ⏳ {mins:02}:{secs:02}
                </div>
            """, unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.remaining_time -= 1

    if st.session_state.remaining_time < 0:
        st.toast("🎉 Time's up! The countdown has finished!", icon="🎉")
    elif not st.session_state.running:
        st.toast("⏹️ Timer Stopped! Click 'Start' to resume.", icon="⚠️")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #4caf50;'>⏳ Stylish Countdown Timer</h1>",
    unsafe_allow_html=True
)

# Input Time
with st.container():
    st.markdown(
        "<p style='font-size: 18px; color: #333;'>Enter time in seconds:</p>", 
        unsafe_allow_html=True
    )
    if not st.session_state.running:
        st.session_state.input_time = st.number_input(
            "", min_value=1, step=1, value=st.session_state.input_time, format="%d",
            key="time_input", help="Countdown time in seconds"
        )

# Custom Button Style
st.markdown("""
    <style>
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            width: 100%;
            transition: 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #388e3c;
        }
    </style>
""", unsafe_allow_html=True)

# Button Layout
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("🚀 Start"):
        countdown_timer()

with col2:
    if st.button("✋ Stop"):
        st.session_state.running = False

with col3:
    if st.button("🔄 Reset"):
        st.session_state.running = False
        st.session_state.remaining_time = st.session_state.input_time
        st.toast("🔁 Timer reset!", icon="⏱️")
