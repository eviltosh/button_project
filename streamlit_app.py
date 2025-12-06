import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Hidden state variable
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# Sidebar CSS + neon buttons
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
        background-size: cover;
        background-position: center;
    }
    .neon-close {
        position: absolute;
        top: 40px;
        right: 30px;
        padding: 10px 22px;
        font-weight: 800;
        color: white;
        background: #a000ff;
        border-radius: 8px;
        border: 2px solid #ff66ff;
        box-shadow: 0 0 20px #a000ff;
        cursor: pointer;
    }
    .neon-open {
        position: fixed;
        top: 40px;
        left: 40px;
        padding: 10px 22px;
        font-weight: 800;
        color: white;
        background: #00ff66;
        border-radius: 8px;
        border: 2px solid #00ff99;
        box-shadow: 0 0 20px #00ff66;
        cursor: pointer;
        z-index: 999999;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------
# SIDEBAR CONTENT
# ----------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        st.write(" ")
        st.write(" ")

        components.html("""
            <button class="neon-close" onclick="parent.postMessage({type:'CLOSE_SIDEBAR'}, '*')">
                CLOSE
            </button>
            """,
            height=80,
        )


# ----------------------
# OPEN BUTTON OUTSIDE
# ----------------------
if not st.session_state.sidebar_open:
    components.html("""
        <button class="neon-open" onclick="parent.postMessage({type:'OPEN_SIDEBAR'}, '*')">
            OPEN SIDEBAR
        </button>
        """,
        height=80,
    )

# ----------------------
# JS HANDLER
# ----------------------
components.html("""
<script>
window.addEventListener("message", (event) => {
    if (event.data.type === "CLOSE_SIDEBAR") {
        window.parent.location.reload();
    }
    if (event.data.type === "OPEN_SIDEBAR") {
        window.parent.location.reload();
    }
});
</script>
""", height=0)


# ----------------------
# MAIN AREA
# ----------------------
st.title("Main App")
st.write("Sidebar toggle is working with neon buttons.")
