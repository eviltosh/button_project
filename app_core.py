import streamlit as st

# Force sidebar expanded
st.set_page_config(initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR PURPLE NEON BUTTON ---
st.markdown("""
    <style>
    /* Sidebar container */
    [data-testid="stSidebar"] {
        background-color: #0b0b0f;
        padding-top: 20px;
        position: relative;
    }

    /* Container for right-aligned button */
    .neon-btn-container {
        position: absolute;
        top: 10px;
        right: 15px;
        z-index: 9999;
    }

    /* Neon purple button */
    .neon-btn {
        padding: 8px 18px;
        color: white;
        background: #7d00ff;
        border: 2px solid #c878ff;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
        text-shadow: 0 0 8px #d18dff;
        box-shadow: 0 0 12px #b14fff, 0 0 20px #7d00ff;
        transition: 0.2s ease-in-out;
    }

    .neon-btn:hover {
        box-shadow: 0 0 20px #c878ff, 0 0 40px #a040ff;
        transform: scale(1.06);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.markdown("""
        <div class="neon-btn-container">
            <button class="neon-btn" onclick="window.location.href='#'">PRESS</button>
        </div>
    """, unsafe_allow_html=True)

    st.header("Sidebar Content")
    st.write("Operational neon button online, Corporal.")

# Main app
st.title("Neon Button Test App")
st.write("Sidebar with top-right neon button loaded successfully.")
