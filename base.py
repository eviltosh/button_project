import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(initial_sidebar_state="expanded")

# session flag so we can show status
if "sidebar_closed" not in st.session_state:
    st.session_state.sidebar_closed = False

# -----------------------------------------------------------------------------
# JS: multi-strategy sidebar closer + restorer
# - tries clicking native toggle
# - tries walking up iframe parents to find [data-testid="stSidebar"]
# - sets width/min/max/overflow/pointerEvents to "close"
# - also sends window.postMessage as a fallback for wrapper layers
# -----------------------------------------------------------------------------
sidebar_control_js = r"""
<script>
(function(){
    // collapse function: tries many strategies
    window.forceCloseSidebar = function() {
        let tried = {
            toggleClick: false,
            domWalk: false,
            postMsg: false
        };

        // 1) Try to click known Streamlit toggle buttons
        try {
            // by title
            const titleToggle = document.querySelector("button[title='Collapse sidebar'], button[title='Toggle sidebar']");
            if (titleToggle) { titleToggle.click(); tried.toggleClick = true; return; }

            // by aria-labels or role
            const roleToggle = document.querySelector("button[aria-label*='Collapse'], button[aria-label*='Toggle']");
            if (roleToggle) { roleToggle.click(); tried.toggleClick = true; return; }

            // fallback: find button with svg that looks like chevron
            const btns = Array.from(document.querySelectorAll("button"));
            for (let b of btns) {
                if (b.innerText && b.innerText.trim().toLowerCase().includes('sidebar')) { b.click(); tried.toggleClick = true; return; }
            }
        } catch(e){ /* ignore */ }

        // 2) Climb up frame/parent chain to locate the real sidebar element
        try {
            let doc = document;
            let attempts = 0;
            while (doc && attempts < 12) {
                const sidebar = doc.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    // store previous inline styles as data attribute so we can restore later
                    if (!sidebar.dataset._savedStyle) {
                        sidebar.dataset._savedStyle = sidebar.getAttribute('style') || '';
                    }
                    sidebar.style.width = "0px";
                    sidebar.style.minWidth = "0px";
                    sidebar.style.maxWidth = "0px";
                    sidebar.style.overflow = "hidden";
                    sidebar.style.pointerEvents = "none";
                    // also collapse any parent column widths if Streamlit set them inline
                    try {
                        const wrapper = sidebar.closest('[role="complementary"], .css-1d391kg, .css-1lcbmhc');
                        if (wrapper) {
                            if (!wrapper.dataset._savedStyle) wrapper.dataset._savedStyle = wrapper.getAttribute('style') || '';
                            wrapper.style.width = "0px";
                            wrapper.style.minWidth = "0px";
                            wrapper.style.maxWidth = "0px";
                            wrapper.style.pointerEvents = "none";
                        }
                    } catch(e){}
                    tried.domWalk = true;
                    return;
                }
                // attempt to go up one level
                try {
                    if (doc.defaultView && doc.defaultView.parent && doc.defaultView.parent.document && doc.defaultView.parent !== window) {
                        doc = doc.defaultView.parent.document;
                    } else {
                        break;
                    }
                } catch(e){
                    // cross-origin or security blo
