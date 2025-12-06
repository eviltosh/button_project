import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Neon Sidebar Control", layout="wide", initial_sidebar_state="expanded")

# ---------------------------------------------------------------------
# Helper: read current 'sidebar' param to decide open/closed state
# - "open" (default) or "closed"
# ---------------------------------------------------------------------
params = st.experimental_get_query_params()
sidebar_state = params.get("sidebar", ["open"])[0]

# ---------------------------------------------------------------------
# JS utilities (single triple-quoted string, but JS avoids nested triple quotes)
# - functions: tryToggleSidebar(), forceCloseSidebar(), forceOpenSidebar()
# - These try multiple strategies so it works across embed layers
# ---------------------------------------------------------------------
control_js = """
<script>
(function(){
    window.tryToggleSidebar = function() {
        // Try to click any Streamlit toggle buttons by known attributes
        try {
            const t1 = document.querySelector("button[title='Collapse sidebar']");
            const t2 = document.querySelector("button[title='Toggle sidebar']");
            const t3 = document.querySelector("button[title='Expand sidebar']");
            if (t1) { t1.click(); return true; }
            if (t2) { t2.click(); return true; }
            if (t3) { t3.click(); return true; }
        } catch(e){}

        return false;
    };

    window.forceCloseSidebar = function() {
        // 1) try toggle
        try {
            if (window.tryToggleSidebar()) return true;
        } catch(e) {}

        // 2) climb frames to find sidebar and set its display/width to hide
        try {
            let doc = document;
            for (let i = 0; i < 12; i++) {
                const sidebar = doc.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    if (!sidebar.dataset._savedStyle) sidebar.dataset._savedStyle = sidebar.getAttribute('style') || '';
                    sidebar.style.display = 'none';
                    sidebar.style.width = '0px';
                    sidebar.style.minWidth = '0px';
                    sidebar.style.pointerEvents = 'none';
                    return true;
                }
                try { doc = doc.defaultView.parent.document; } catch(e){ break; }
            }
        } catch(e){}

        // 3) postMessage fallback (for wrappers)
        try {
            window.parent.postMessage({type:'streamlit:closeSidebar'}, "*");
            return true;
        } catch(e){}

        return false;
    };

    window.forceOpenSidebar = function() {
        // 1) try toggle
        try {
            if (window.tryToggleSidebar()) return true;
        } catch(e){}

        // 2) climb frames to find sidebar and restore saved style or clear display overrides
        try {
            let doc = document;
            for (let i = 0; i < 12; i++) {
                const sidebar = doc.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    if (sidebar.dataset._savedStyle !== undefined) {
                        sidebar.setAttribute('style', sidebar.dataset._savedStyle || '');
                        delete sidebar.dataset._savedStyle;
                    } else {
                        sidebar.style.display = '';
                        sidebar.style.width = '';
                        sidebar.style.minWidth = '';
                        sidebar.style.pointerEvents = '';
                    }
                    return true;
                }
                try { doc = doc.defaultView.parent.document; } catch(e){ break; }
            }
        } catch(e){}

        // 3) postMessage fallback
        try {
            window.parent.postMessage({type:'streamlit:openSidebar'}, "*");
            return true;
        } catch(e){}

        return false;
    };

    // Listen for messages from other frames/wrappers:
    window.addEventListener('message', function(ev){
        try {
            const d = ev.data || {};
            if (d && d.type === 'streamlit:doCloseSidebar') window.forceCloseSidebar();
            if (d && d.type === 'streamlit:doOpenSidebar') window.forceOpenSidebar();
        } catch(e){}
    }, false);
})();
</script>
"""
components.html(control_js, height=0, width=0)

# ---------------------------------------------------------------------
# Sidebar: inject purple neon close button only when sidebar_state == 'open'
# We inject inside the sidebar so it appears top-right there.
# ---------------------------------------------------------------------
if sidebar_state == "open":
    # Purple neon close button HTML/CSS — exact appearance preserved
    sidebar_html = """
    <style>
    /* ensure wrapper area so layout isn't broken */
    #purple-close-wrapper {
        position: relative;
        min-height: 48px;
        pointer-events: none; /* parent not interactive so Streamlit doesn't intercept */
    }
    #purple-close-btn {
        position: absolute;
        top: 10px;
        right: 12px;
        z-index: 9999;
        background: #9b4dff;
        color: white;
        border: none;
        padding: 9px 16px;
        border-radius: 10px;
        font-weight: 800;
        cursor: pointer;
        box-shadow: 0 0 12px rgba(160,32,240,0.85), 0 0 22px rgba(180,120,255,0.45);
        pointer-events: auto; /* button itself is interactive */
        font-family: "Segoe UI", Roboto, Arial, sans-serif;
    }
    #purple-close-btn:hover { transform: scale(1.03); }
    #purple-close-btn:active { transform: scale(.99); }
    </style>

    <div id="purple-close-wrapper">
        <button id="purple-close-btn" onclick="
            (function(){
                try{ window.forceCloseSidebar(); }catch(e){}
                // update URL to tell Streamlit server sidebar is closed
                try {
                    const params = new URLSearchParams(window.location.search);
                    params.set('sidebar', 'closed');
                    window.location.search = params.toString();
                } catch(e){}
            })();
        ">✖ Close</button>
    </div>
    """
    # render inside the sidebar
    components.html(sidebar_html, height=70)

    # Also show some sidebar content under it so it looks natural
    with st.sidebar:
        st.write("Sidebar Online — Purple close button at top-right.")

# ---------------------------------------------------------------------
# Main page: GREEN open button appears only when sidebar_state == 'closed'
# We position it top-right of the main page (floating)
# ---------------------------------------------------------------------
if sidebar_state == "closed":
    open_html = """
    <style>
    #green-open-btn {
        position: fixed;
        top: 16px;
        right: 22px;
        z-index: 10000;
        background: #1fa12f;
        color: white;
        border: none;
        padding: 10px 18px;
        border-radius: 10px;
        font-weight: 700;
        cursor: pointer;
        box-shadow: 0 4px 14px rgba(31,161,47,0.25);
        font-family: "Segoe UI", Roboto, Arial, sans-serif;
    }
    #green-open-btn:hover { transform: translateY(-1px); }
    </style>

    <button id="green-open-btn" onclick="
        (function(){
            try{ window.forceOpenSidebar(); }catch(e){}
            try {
                const params = new URLSearchParams(window.location.search);
                params.set('sidebar','open');
                window.location.search = params.toString();
            } catch(e){}
        })();
    ">Open Sidebar</button>
    """
    st.markdown(open_html, unsafe_allow_html=True)

# ---------------------------------------------------------------------
# Main page content (always shown). Provide an explicit reopen control too if needed.
# ---------------------------------------------------------------------
st.title("Neon Sidebar Control Test")
st.write("Use the green Open button (top-right) to expand the sidebar, or the purple Close inside the sidebar to collapse it.")

# For convenience, also show a small actionable control (non-primary):
if st.button("Force Reopen (server-side)"):
    # server-side attempt: emit a small JS to open and reload params to open
    components.html("<script>try{ window.forceOpenSidebar(); }catch(e){} try{ window.parent.postMessage({type:'streamlit:openSidebar'}, '*'); }catch(e){} </script>", height=0)
    # set params so on reload Streamlit sees open
    params = st.experimental_get_query_params()
    params["sidebar"] = ["open"]
    st.experimental_set_query_params(**params)
    st.experimental_rerun()
