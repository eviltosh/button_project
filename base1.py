import streamlit as st

# -------------------------
# SESSION STATE
# -------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# -------------------------
# BASE CSS
# -------------------------
st.markdown("""
<style>

    /* Sidebar transition */
    [data-testid="stSidebar"] {
        transition: all 0.25s ease-in-out;
    }

    /* Purple neon button */
    .neon-purple button {
        background-color: #b300ff !important;
        color: white !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #ff00ff, 0 0 20px #b300ff !important;
    }

    /* Green neon button */
    .neon-green button {
        background-color: #00ff00 !important;
        color: black !important;
        border: 2px solid #00ffaa !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #00ff00, 0 0 20px #00aa00 !important;
    }

</style>
""", unsafe_allow_html=True)


# -------------------------
# SIDEBAR OPEN
# -------------------------
if st.session_state.sidebar_open:

    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 300px !important;
            min-width: 300px !important;
            visibility: visible !important;
        }
        .sidebar-top-right {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 999;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<div class="sidebar-top-right neon-purple">', unsafe_allow_html=True)
        if st.button("Close"):
            # Fix: instant collapse (1 click)
            st.markdown("""
                <script>
                    const sb = window.parent.document.querySelector('section[data-testid="stSidebar"]');
                    if (sb) { sb.style.transform = "translateX(-100%)"; }
                </script>
            """, unsafe_allow_html=True)

            st.session_state.sidebar_open = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# -------------------------
# SIDEBAR CLOSED
# -------------------------
else:

    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 0 !important;
            min-width: 0 !important;
            visibility: hidden !important;
        }
        .green-floating {
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 2000;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="green-floating neon-green">', unsafe_allow_html=True)
    if st.button("Open"):

        # Fix: instant expand (1 click)
        st.markdown("""
            <script>
                const sb = window.parent.document.querySelector('section[data-testid="stSidebar"]');
                if (sb) { sb.style.transform = "translateX(0)"; }
            </script>
        """, unsafe_allow_html=True)

        st.session_state.sidebar_open = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------
# MAIN CONTENT
# -------------------------
st.title("Sidebar Toggle Test")
st.write("Purple button = collapse. Green button = expand.")

