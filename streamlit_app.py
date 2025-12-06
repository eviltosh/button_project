import streamlit as st

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# --- APPLY SIDEBAR BACKGROUND ---
sidebar_css = f"""
<style>
[data-testid="stSidebar"] > div:first-child {{
    background-image: url('{RAW_URL}');
    background-size: cover;
    background-position: center;
}}

.sidebar-button {{
    position: absolute;
    top: 12px;
    right: 12px;
    padding: 8px 14px;
    background: #9500ff;
    border-radius: 8px;
    border: 2px solid #f0caff;
    font-weight: bold;
    color: white;
    cursor: pointer;
}}
</style>
"""

st.markdown(sidebar_css, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown(f"<div class='sidebar-button'>CLOSE</div>", unsafe_allow_html=True)

# --- MAIN SCREEN BUTTON ---
st.markdown(
    """
    <style>
    .main-open {
        position: fixed;
        top: 12px;
        right: 12px;
        padding: 10px 16px;
        background: #38ff38;
        border: 2px solid #aaffaa;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
    }
    </style>
    <div class="main-open">OPEN SIDEBAR</div>
    """,
    unsafe_allow_html=True
)

st.title("Main App")
