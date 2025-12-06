import streamlit as st

st.set_page_config(layout="wide")

# ---------------------------------------------
# CSS: Neon purple button (fully clickable)
# ---------------------------------------------
st.markdown("""
<style>
/* Sidebar container override */
section[data-testid="stSidebar"] {
    width: 300px !important;
}

/* WRAPPER to isolate the button from Streamlit's sidebar DOM */
#neon-btn-wrapper {
    position: relative;
    width: 100%;
    height: 60px;
    pointer-events: none;  /* parent NON-interactive */
}

/* Actual neon button */
#neon-btn {
    position: absolute;
    top: 10px;
    right: 10px;

    background: #a020f0;
    color: white;
    border: none;
    padding: 10px 18px;

    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;

    cursor: pointer;
    box-shadow: 0 0 12px #d26bff, 0 0 24px #a020f0;

    pointer-events: auto;  /* BUT button IS interactive */
}

#neon-btn:hover {
    box-shadow: 0 0 16px #ff7aff, 0 0 32px #b152ff;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------
# JS: Communicate button click → Streamlit
# ---------------------------------------------
st.markdown("""
<script>
function neonClick() {
    window.parent.postMessage({button: "pressed"}, "*");
}
</script>
""", unsafe_allow_html=True)

# ---------------------------------------------
# Sidebar UI
# ---------------------------------------------
with st.sidebar:
    st.markdown("""
    <div id="neon-btn-wrapper">
        <button id="neon-btn" onclick="neonClick()">✖ Close</button>
    </div>
    """, unsafe_allow_html=True)

    st.write("Sidebar Online, Major Tom.")


# ---------------------------------------------
# Listen for message from JS
# ---------------------------------------------
msg = st.experimental_get_query_params().get("button-state", [""])[0]

st.title("Neon Sidebar Control Test")

# Script to listen in browser
st.markdown("""
<script>
window.addEventListener("message", (event) => {
    if (event.data.button === "pressed") {
        const query = new URLSearchParams(window.location.search);
        query.set("button-state", "pressed");
        window.location.search = query.toString();
    }
});
</script>
""", unsafe_allow_html=True)

if msg == "pressed":
    st.success("Close button pressed.")
else:
    st.info("Waiting for input…")
