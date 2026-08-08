import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="Vikas Mishra | Ultra Recovery Pro",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit Default Top Header & Footer Padding
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

# Function to read HTML File
def load_html_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>Error: index.html file not found!</h3>"

# Render custom HTML/CSS/JS inside Streamlit
html_content = load_html_file("index.html")
components.html(html_content, height=1000, scrolling=True)
