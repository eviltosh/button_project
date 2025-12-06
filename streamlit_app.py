import streamlit as st

st.set_page_config(layout="wide")

# Your confirmed background image
BG_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# -------------------------------------------------------------
# SESSION STATE
# -------------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# -------------------------------------------------------------
# SIDEBAR (OPEN STATE)
# -------------------------------------------------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        # Background layer — DOES NOT BLOCK CLICKS
        st.markdown(
            f"""
            <div style="
                position:absolute;
                inset:0;
                background:url('{BG_URL}') center/cover no-repeat;
                z-index:0;
                pointer-events:none;
            "></div>
            """,
            unsafe_allow_html=True
        )

        # Neon purple CLOSE button
        st.markdown(
            """
            <style>
            .purple-close {
                background:#b300ff;
                color:white !important;
                width:100%;
                padding:12px 20px;
                border:none;
                border-radius:8px;
                font-weight:700;
                box-shadow:0 0 12px #b300ff;
                cursor:pointer;
                position:relative;
                z-index:10;
            }
            .purple-close:hover {
                box-shadow:0 0 22px #d36bff;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button("CLOSE", key="close_btn"):
            st.session_state.sidebar_open = False

# -------------------------------------------------------------
# MAIN PAGE — OPEN BUTTON (ONLY WHEN SIDEBAR CLOSED)
# -------------------------------------------------------------
if not st.session_state.sidebar_open:
    st.markdown(
        """
        <style>
        .green-open {
            background:#00ff88;
            color:black !important;
            padding:12px 22px;
            font-weight:700;
            border:none;
            border-radius:8px;
            box-shadow:0 0 12px #00ff88;
            cursor:pointer;

            /* Position top-right BELOW Streamlit black menu bar */
            position:fixed;
            top:70px;
            right:25px;
            z-index:9999;
        }
        .green-open:hover {
            box-shadow:0 0 22px #66ffc2;
        }
        </style>

        <button class="green-open" onclick="window.location.search='open=1'">
            OPEN
        </button>
        """,
        unsafe_allow_html=True
    )

# Handle open via query param
query = st.query_params.to_dict()
if "open" in query:
    st.session_state.sidebar_open = True

# -------------------------------------------------------------
# MAIN PAGE CONTENT
# -------------------------------------------------------------
st.title("Main App")
st.write("Sidebar toggle is fully operational.")
