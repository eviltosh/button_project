import streamlit as st

st.set_page_config(layout="wide")

# --- Inject Custom CSS + Sidebar + Buttons ---
custom_html = """
<style>
/* Sidebar container */
#customSidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 260px;
    height: 100vh;
    background: rgba(20, 20, 30, 0.95);
    box-shadow: 4px 0 20px rgba(0,0,0,0.6);
    backdrop-filter: blur(10px);
    transform: translateX(-100%);
    transition: 0.35s ease-in-out;
    z-index: 99998;
}

/* Visible sidebar state */
#customSidebar.visible {
    transform: translateX(0);
}

/* Purple Neon Close Button */
#closeBtn {
    position: absolute;
    top: 20px;
    right: 20px;
    background: #b26bff;
    padding: 10px 22px;
    border-radius: 12px;
    font-weight: 600;
    color: white;
    cursor: pointer;
    box-shadow: 0 0 18px #b26bff;
    transition: 0.2s ease;
}
#closeBtn:hover {
    box-shadow: 0 0 32px #d5a7ff;
}

/* Green OPEN Button (top-left) */
#openBtn {
    position: fixed;
    top: 20px;
    left: 20px;
    background: #00ff88;
    padding: 12px 26px;
    border-radius: 12px;
    font-weight: 700;
    color: black;
    cursor: pointer;
    box-shadow: 0 0 14px #00ff88;
    z-index: 99999;
}
#openBtn.hidden {
    display: none;
}
</style>

<div id="openBtn">OPEN SIDEBAR</div>

<div id="customSidebar">
    <div id="closeBtn">✕ Close</div>
</div>

<script>
const sidebar = document.getElementById("customSidebar");
const openBtn = document.getElementById("openBtn");
const closeBtn = document.getElementById("closeBtn");

// OPEN
openBtn.onclick = () => {
    sidebar.classList.add("visible");
    openBtn.classList.add("hidden");
};

// CLOSE
closeBtn.onclick = () => {
    sidebar.classList.remove("visible");
    openBtn.classList.remove("hidden");
};
</script>

"""

st.markdown(custom_html, unsafe_allow_html=True)

# Main app content (no explanatory text anymore)
st.write("")
