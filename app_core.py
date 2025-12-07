import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# --------------------------------------------------------
# STATE CONTROL
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

params = st.query_params
if "sidebar" in params:
    st.session_state.sidebar_open = params.get("sidebar") == "1"


# --------------------------------------------------------
# CSS — SAFE, SINGLE-STRING (NO TRIPLE QUOTES)
# --------------------------------------------------------
css = """
<style>

/* Remove Streamlit sidebar */
section[data-testid="stSidebar"] { display:none !important; }
div[data-testid="collapsedControl"] { display:none !important; }

/* Main neon button */
a.neon {
  display:inline-block;
  background:linear-gradient(135deg,#9b00ff,#b300ff);
  padding:12px 20px;
  border-radius:12px;
  color:#fff !important;
  font-weight:700;
  border:2px solid #b300ff;
  box-shadow:0 0 12px #b300ff,0 0 28px rgba(
