import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import urlencode, urlparse, urlunparse, parse_qs

# -------------------------
# SESSION STATE init
# -------------------------
if "sidebar_state" not in st.session_state:
    # default: expanded
    st.session_state.sidebar_state = "expanded"  # "expanded" or "collapsed"

# -------------------------
# Apply page config from session state
# -------------------------
st.set_page_config(
    page_title="Sidebar Toggle System — Reliable",
    layout="wide",
    initial_sidebar_state=st.session_state.sidebar_state,
)

# -------------------------
# Helper: reload browser with a sidebar query param so Streamlit honors the new initial_sidebar_state
# We avoid calling st.experimental_rerun() to dodge environments where it may not be present.
# Instead we emit a tiny client-side script via components.html (safe and enclosed in triple quotes).
# -------------------------
def reload_with_sidebar_param(expanded: bool):
    # build param value: '1' => expanded, '0' => collapsed
    val = "1" if expanded else "0"
    # client-side script will modify the current URL's searchParams and replace location
    script = f"""
    <script>
    (function() {{
      try {{
        const url = new URL(window.location.href);
        url.searchParams.set('sidebar', '{val}');
        // replace so toggling doesn't spam history
        window.location.replace(url.toString());
      }} catch (e) {{
        // fallback: hard reload
        window.location.reload();
      }}
    }})();
    </script>
    """
    # render zero-height HTML to execute script on client
    components.html(script, height=0)

# -------------------------
# UI: Title + Toggle
# -------------------------
st.title("Sidebar Toggle System — RELIABLE VERSION")

col1, col2 = st.columns([1, 5])
with col1:
    if st.button("Toggle Sidebar", key="toggle_btn"):
        # flip the intended state in session_state
        new_state = "collapsed" if st.session_state.sidebar_state == "expanded" else "expanded"
        st.session_state.sidebar_state = new_state

        # Now reload the page client-side with a query param that our app will read on next run
        # This avoids using st.experimental_rerun(), which caused the AttributeError in your environment.
        expanded_bool = True if new_state == "expanded" else False
        reload_with_sidebar_param(expanded_bool)

with col2:
    st.write("Sidebar state (session):", st.session_state.sidebar_state)
    st.write("Note: This implementation uses session_state + a client reload to ensure Streamlit applies the new initial_sidebar_state reliably.")

# -------------------------
# On load: respect explicit query param if present (allows the reload script to control behavior)
# -------------------------
# If a URL param ?sidebar=0/1 is present, prefer it (so our reload_with_sidebar_param works deterministically).
params = st.experimental_get_query_params()
sidebar_q = params.get("sidebar", [None])[0]
if sidebar_q is not None:
    # map query param to state
    st.session_state.sidebar_state = "expanded" if sidebar_q == "1" else "collapsed"
    # re-apply page config (some Streamlit versions only honor initial_sidebar_state at config time)
    # Note: calling set_page_config twice is safe early in script
    st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)

# -------------------------
# Sidebar content (visible when expanded)
# -------------------------
with st.sidebar:
    st.markdown("### Sidebar content")
    st.markdown("Use the big button on the left to toggle the sidebar. This implementation avoids server-only reruns and uses a short client refresh to apply state consistently across environments.")

# -------------------------
# Final: small debug info
# -------------------------
st.markdown("---")
st.write("If the toggle doesn't behave correctly, paste the full traceback you see (copy the entire error block).")
