import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Neon Custom Sidebar (Fixed)", layout="wide")

st.title("Neon Sidebar Control — Custom HTML Sidebar (Method A) — Fixed")
st.write("This version forces the injected HTML iframe to a large height so Streamlit Cloud won't suppress it.")
st.write("Green OPEN button sits top-left. Purple CLOSE is top-right inside the sidebar. One visible at a time.")

# ----------------------------------------------------------------
# Self-contained HTML/CSS/JS for the custom sidebar + buttons
# ----------------------------------------------------------------
html = """
<style>
:root{
  --sidebar-width: 320px;
  --bg-dark: #0b0b0f;
}

/* OPEN BUTTON (green) top-left */
#neon-open-btn {
  position: fixed;
  top: 18px;
  left: 18px;
  z-index: 999999;
  background: linear-gradient(90deg,#00ff9f,#00d67a);
  color: #001100;
  padding: 12px 18px;
  border-radius: 12px;
  border: none;
  font-weight: 800;
  letter-spacing: 0.6px;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(0,255,159,0.15), 0 0 36px rgba(0,214,122,0.08);
  transition: transform 120ms ease;
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
}
#neon-open-btn:active { transform: translateY(1px) scale(.995); }
#neon-open-btn.hidden { display: none; }

/* SIDEBAR container */
#customSidebar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: var(--sidebar-width);
  max-width: 90vw;
  background: linear-gradient(180deg,#23232a, #17171b);
  box-shadow: 8px 0 30px rgba(0,0,0,0.6);
  transform: translateX(-110%);
  transition: transform 300ms cubic-bezier(.2,.9,.2,1);
  z-index: 999998;
  display: flex;
  flex-direction: column;
  padding: 18px;
  color: #e8e8ee;
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
}

/* When open */
#customSidebar.open {
  transform: translateX(0);
}

/* Header row inside sidebar to hold purple close button */
#cs-header {
  position: relative;
  min-height: 44px;
  margin-bottom: 8px;
}

/* Purple neon close button (exact look preserved) */
#purple-close {
  position: absolute;
  top: 0;
  right: 0;
  background: #9b4dff;
  padding: 9px 16px;
  border-radius: 10px;
  border: none;
  font-weight: 800;
  color: white;
  cursor: pointer;
  box-shadow: 0 0 12px rgba(160,32,240,0.85), 0 0 22px rgba(180,120,255,0.45);
  pointer-events: auto;
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
}
#purple-close:hover { transform: scale(1.03); }
#purple-close:active { transform: scale(.98); }

/* Content area */
#cs-content {
  padding-top: 8px;
  overflow-y: auto;
}

/* Important: allow pointer events in the injected sidebar */
#customSidebar, #customSidebar * { pointer-events: auto; }

/* Hide built-in Streamlit sidebar if present (safe fallback) */
section[data-testid="stSidebar"]{ display:none !important; }

/* Responsive tweak */
@media (max-width: 520px) {
  :root { --sidebar-width: 86vw; }
  #neon-open-btn { left: 12px; top: 12px; padding: 10px 14px; }
}
</style>

<!-- Sidebar DOM -->
<div id="customSidebar" aria-hidden="true">
  <div id="cs-header">
    <button id="purple-close" aria-label="Close sidebar">✖ Close</button>
  </div>

  <div id="cs-content">
    <h3 style="margin:6px 0 12px 0;">Sidebar Panel</h3>
    <p style="margin:0 0 10px 0;color:#cfcfe0;">Operational neon button online, Major Tom.</p>

    <div style="margin-top:12px;">
      <label style="display:block;margin-bottom:6px;color:#bfc0d8;">Example control</label>
      <button style="
          padding:8px 12px;
          border-radius:8px;
          border:1px solid rgba(255,255,255,0.06);
          background:linear-gradient(180deg,#2b2b33,#222227);
          color:#fff;
          cursor:pointer;
          ">Action</button>
    </div>

    <div style="margin-top:20px;color:#9fa0b8;font-size:13px;">
      <p>Put your app settings, toggles, or anything here.</p>
    </div>
  </div>
</div>

<!-- Green open button top-left -->
<button id="neon-open-btn" aria-label="Open sidebar">OPEN SIDEBAR</button>

<script>
(function(){
  const openBtn = document.getElementById('neon-open-btn');
  const sidebar = document.getElementById('customSidebar');
  const closeBtn = document.getElementById('purple-close');

  function openSidebar() {
    sidebar.classList.add('open');
    sidebar.setAttribute('aria-hidden', 'false');
    openBtn.classList.add('hidden');
  }
  function closeSidebar() {
    sidebar.classList.remove('open');
    sidebar.setAttribute('aria-hidden', 'true');
    setTimeout(()=> openBtn.classList.remove('hidden'), 260);
  }

  openBtn.addEventListener('click', function(e){
    e.stopPropagation();
    openSidebar();
  });

  closeBtn.addEventListener('click', function(e){
    e.stopPropagation();
    closeSidebar();
  });

  // close when clicking outside
  document.addEventListener('click', function(e){
    const outside = !sidebar.contains(e.target) && !openBtn.contains(e.target);
    if (outside && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  }, true);

  // ESC to close
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  });

  // start closed (if you want open by default, call openSidebar())
})();
</script>
"""

# ----------------------------------------------------------------
# CRITICAL FIX: force a tall iframe so Streamlit Cloud shows the component
# ----------------------------------------------------------------
components.html(html, height=800, scrolling=False)

# ----------------------------------------------------------------
# Continue Streamlit-managed content below
# ----------------------------------------------------------------
st.write("Main app area — your Streamlit widgets go here below the injected custom sidebar.")
st.write("If anything still looks off visually, say ‘Failure’ and paste a screenshot — I will consult GH, SO and the USEReady blog (and others) FIRST, then patch immediately.")
