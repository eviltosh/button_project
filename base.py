import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Neon Custom Sidebar (Fixed)", layout="wide")

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

/* Header row inside sidebar */
#cs-header {
  position: relative;
  min-height: 44px;
  margin-bottom: 8px;
}

/* Purple neon close button */
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

#cs-content {
  padding-top: 8px;
  overflow-y: auto;
}

/* Allow interaction */
#customSidebar, #customSidebar * { pointer-events: auto; }

/* Hide Streamlit's built-in sidebar */
section[data-testid="stSidebar"]{ display:none !important; }

@media (max-width: 520px) {
  :root { --sidebar-width: 86vw; }
  #neon-open-btn { left: 12px; top: 12px; padding: 10px 14px; }
}
</style>

<div id="customSidebar" aria-hidden="true">
  <div id="cs-header">
    <button id="purple-close" aria-label="Close sidebar">✖ Close</button>
  </div>

  <div id="cs-content">
    <!-- Your sidebar content goes here -->
  </div>
</div>

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

  document.addEventListener('click', function(e){
    const outside = !sidebar.contains(e.target) && !openBtn.contains(e.target);
    if (outside && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  }, true);

  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  });

})();
</script>
"""

components.html(html, height=800, scrolling=False)
