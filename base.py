import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html = """
<style>
:root { --sidebar-width: 320px; }

/* Sidebar container with GitHub-hosted background image */
#customSidebar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: var(--sidebar-width);
  background: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png') center/cover no-repeat;
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
#customSidebar.open { transform: translateX(0); }

/* Purple close button styling */
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
}
#purple-close:hover { transform: scale(1.03); }
#purple-close:active { transform: scale(.98); }

/* Sidebar content area */
#cs-content { margin-top: 44px; overflow-y: auto; }

/* Hide default sidebar if exists */
section[data-testid="stSidebar"] { display: none !important; }
</style>

<div id="customSidebar" aria-hidden="true">
  <button id="purple-close">✖ Close</button>
  <div id="cs-content">
    <!-- YOUR SIDEBAR CONTENT HERE -->
    <h3>Menu</h3><p>Controls go here</p>
  </div>
</div>

<button id="neon-open-btn" style="
  position: fixed; top: 18px; left: 18px;
  padding: 12px 18px; background: #00ff9f;
  border: none; border-radius: 12px; font-weight: 800;
  cursor: pointer; box-shadow: 0 6px 18px rgba(0,255,159,0.3);
  z-index: 999999;
">OPEN SIDEBAR</button>

<script>
const sidebar = document.getElementById('customSidebar');
const openBtn = document.getElementById('neon-open-btn');
const closeBtn = document.getElementById('purple-close');

openBtn.onclick = ()=>{
  sidebar.classList.add('open');
  openBtn.style.display = 'none';
};
closeBtn.onclick = ()=>{
  sidebar.classList.remove('open');
  openBtn.style.display = 'block';
};
</script>
"""

components.html(html, height=800, scrolling=False)
