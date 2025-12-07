import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# ----------------------------------------------------------
# SESSION STATE — handles open/close state
# ----------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True  # default OPEN


# ----------------------------------------------------------
# CSS — completely hides Streamlit default sidebar
# ----------------------------------------------------------
st.markdown("""
<style>

    /* Hide built-in Streamlit sidebar and its chevron */
    section[data-testid="stSidebar"] { display: none !important; }
    div[data-testid="collapsedControl"] { display: none !important; }

    /* Neon button global style */
    div.stButton > button {
        background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%) !important;
        color: #fff !important;
        border-radius: 12px !important;
        padding: 10px 22px !important;
        font-weight: 700 !important;
        border: 2px solid #b300ff !important;
        box-shadow: 0 10px 30px rgba(179,0,255,0.32),
                    0 0 36px rgba(179,0,255,0.22) inset !important;
        cursor: pointer;
        transition: 0.15s ease-out !important;
    }

    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.03) !important;
    }

    /* Sidebar container */
    .sidebar-box {
        background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
        padding: 20px;
        position: relative;
        color: white;
    }

</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------
# SIDEBAR OPEN VIEW
# ----------------------------------------------------------
if st.session_state.sidebar_open:

    left_col, right_col = st.columns([1, 4])

    # SIDEBAR AREA
    with left_col:

        st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)

        # CLOSE BUTTON top-right INSIDE sidebar
        c1, c2 = st.columns([4, 1])
        with c2:
            if st.button("CLOSE"):
                st.session_state.sidebar_open = False

        # Sidebar content
        st.markdown("""
        <div style="margin-top: 30px; font-size: 24px; font-weight: 800;">
            NEON SIDEBAR
        </div>
        """, unsafe_allow_html=True)
        st.write("Sidebar content goes here.")
        st.write("Everything inside here stays stable and reliable.")

        st.ma
