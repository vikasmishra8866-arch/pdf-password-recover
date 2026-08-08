import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit Page Configuration
st.set_page_config(
    page_title="Vikas Mishra | Ultra Recovery Pro",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit Default UI Headers & Paddings
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Helper Function to Read index.html
def load_html_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3 style='color:red;'>Error: index.html file not found in directory!</h3>"

# Render Full Custom Deep Ocean UI
html_content = load_html_file("index.html")
components.html(html_content, height=1050, scrolling=True)
