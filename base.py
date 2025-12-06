import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(initial_sidebar_state="expanded")

# -----------------------------------------------------------------------------
# JAVASCRIPT — CLEAN, SINGLE-STRING, NO SYNTAX ERRORS
# -----------------------------------------------------------------------------
sidebar_control_js = """
<script>
window.forceCloseSidebar = function() {
    // 1) Try native toggle buttons by title
    try {
        const t1 = document.querySelector("button[title='Collapse sidebar']");
        const t2 = document.querySelector("button[title='Toggle sidebar']");
        if (t1) { t1.click(); return; }
        if (t2) { t2.click(); return; }
    } catch(e) {}

    // 2) DOM-walk through parent frames to find the actual sidebar
    try {
        let doc = document;
        for (let i = 0; i < 10; i++) {
            const sb = doc.querySelector('[data-testid="stSidebar"]');
            if (sb) {
                sb.style.width = "0px";
                sb.style.minWidth = "0px";
                sb.style.maxWidth = "0px";
                sb.style.overflow = "hidden";
                sb.style.pointerEvents = "none";
                return;
            }
            try { 
                doc = doc.defaultView.parent.document; 
            } catch(e) { 
                break; 
            }
        }
    } catch(e) {}

    // 3) postMessage fallback for Android WebView wrappers
    try { 
        window.parent.postMessage({type:"streamlit:closeSidebar"}, "*"); 
    } catch(e) {}
};

window.restoreSidebar = function() {
    try {
        let doc = document;
        for (let i = 0; i < 10; i++) {
            const sb = doc.querySelector('[data-testid="stSidebar"]');
            if (sb) {
                sb.style.width = "";
                sb.style.minWidth = "";
                sb.style.maxWidth = "";
                sb.style.overflow = "";
                sb.style.pointerEvents = "";
                return;
            }
            try { 
                doc = doc.defaultView.parent.document; 
            } catch(e) { 
                break; 
            }
        }
    } catch(e) {}

    try { 
        window.parent.postMessage({type:"streamlit:restoreSidebar"}, "*"); 
    } catch(e) {}
};
</script>
"""

components.html(sidebar_control_js, height=0, width=0)

# -----------------------------------------------------------------------------
# SIDEBAR WITH NEON CLOSE BUTTON
# -----------------------------------------------------------------------------
with st.sidebar:
    components.html(
        """
        <style>
        .neon-close-btn {
            position: absolute;
            top: 8px;
            right: 10px;
            padding: 8px 14px;
            background: linear-gradient(90deg, #8a2be2, #b57bff);
            border-radius: 10px;
            font-weight: bold;
            color: white;
            cursor: pointer;
            box-shadow: 0 0 12px rgba(160,32,240,0.85), 0 0 20px rgba(180,120,255,0.45);
            border: none;
            font-family: 'Segoe UI', sans-serif;
        }
        .neon-close-btn:hover { transform: scale(1.03); }
        .neon-close-btn:active { transform: scale(.97); }
        </style>

        <button class="neon-close-btn"
            onclick="try{window.forceCloseSidebar();}catch(e){}">
            ✕ Close
        </button>
        """,
        height=50
    )

    st.write("Sidebar Online, Major Tom.")

# -----------------------------------------------------------------------------
# MAIN PAGE
# -----------------------------------------------------------------------------
st.title("Neon Sidebar Control Test")

if st.button("Reopen Sidebar"):
    components.html(
        "<script>try{window.restoreSidebar();}catch(e){}</script>",
        height=0
    )
    st.success("Restore command sent.")

st.write("Sidebar controls loaded.")
