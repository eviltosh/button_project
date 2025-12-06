import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ---------------------------------------------------------
# CSS injector — forces Streamlit to load your repo image
# ---------------------------------------------------------
css = """
<style>

:root { --sidebar-width: 320px; }

#customSidebar {
    background: url('assets/control.png') center/cover no-repeat !important;
}

/* OPEN BUTTON (green) */
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
  cursor: pointer;
}
#neon-open-btn.hidden { display: none; }

/* SIDEBAR */
#customSidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: var(--sidebar-width);
  height: 100vh;
  transform: translateX(-110%);
  transition: transform 300ms ease;
  z-index: 999998;
  padding: 18px;
  color: white;
}

/* When open */
#customSidebar.open { transform: translateX(0); }

#cs-header { position: relative; min-height: 44px; }

#purple-close {
  position: absolute;
  right: 0;
  top: 0;
  background: #9b4dff;
  padding: 9px 16px;
  border-radius: 10px;
  border: none;
  color: white;
  font-weight: 800;
  cursor: pointer;
}

#cs-content {
  margin-top: 16px;
  overflow-y: auto;
}

section[data-testid="stSidebar"] {
    display: none !important;
}

</style>
"""

components.html(css, height=10)

# ---------------------------------------------------------
# Sidebar Structure + JS
# ---------------------------------------------------------
html = """
<div id="customSidebar">
  <div id="cs-header">
    <button id="purple-close">✖ Close</button>
  </div>

  <div id="cs-content">
    <h3>Menu</h3>
    <button style="padding:8px 12px;border-radius:8px;">Action</button>
  </div>
</div>

<button id="neon-open-btn">OPEN SIDEBAR</button>

<script>
const sidebar = document.getElementById('customSidebar');
const openBtn = document.getElementById('neon-open-btn');
const closeBtn = document.getElementById('purple-close');

openBtn.onclick = () => {
    sidebar.classList.add('open');
    openBtn.classList.add('hidden');
};

closeBtn.onclick = () => {
    sidebar.classList.remove('open');
    openBtn.classList.remove('hidden');
};
</script>
"""

components.html(html, height=800, scrolling=False)
