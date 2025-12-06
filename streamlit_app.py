import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

st.title("DEBUG: Sidebar background image diagnostic (run once)")

st.markdown("**Instructions:** Reload the page, wait ~3s for tests to finish. Copy the text results below and paste them back here (or screenshot).")

# 1) Show the URL
st.write("Testing image URL:", RAW_URL)

# --- MAIN HTML (fully enclosed inside triple quotes!) ---
html_code = f"""
<div style="display:flex;gap:18px;align-items:flex-start;">
  <div>
    <div style="font-weight:700;margin-bottom:6px;">Direct &lt;img&gt; test</div>
    <img id="testImg" src="{RAW_URL}" style="max-width:320px; border: 2px solid #222; box-shadow: 0 6px 18px rgba(0,0,0,0.4);" />
    <div id="imgInfo" style="margin-top:8px;color:#ddd;font-family:monospace;"></div>
  </div>

  <div>
    <div style="font-weight:700;margin-bottom:6px;">CSS background test (sidebar preview)</div>
    <div id="bgPreview" style="width:320px;height:240px;border:2px solid #222;background:url('{RAW_URL}') center/cover no-repeat;"></div>
    <div id="bgInfo" style="margin-top:8px;color:#ddd;font-family:monospace;"></div>
  </div>

  <div style="min-width:300px;">
    <div style="font-weight:700;margin-bottom:6px;">Fetch/CORS test (JavaScript)</div>
    <pre id="fetchInfo" style="background:#071018;color:#9fe9c7;padding:10px;border-radius:6px;min-height:120px;overflow:auto;font-family:monospace;"></pre>
  </div>
</div>

<script>
(function(){
  const testImg = document.getElementById('testImg');
  const imgInfo = document.getElementById('imgInfo');
  const fetchInfo = document.getElementById('fetchInfo');
  const bgInfo = document.getElementById('bgInfo');

  // IMG load check
  testImg.onload = function(){
    imgInfo.innerText = 'IMG LOAD OK — naturalW x naturalH = ' +
      this.naturalWidth + ' x ' + this.naturalHeight;
  };
  testImg.onerror = function(){
    imgInfo.innerText = 'IMG LOAD ERROR — network or 404 or CORS issue';
  };

  // Fetch test
  (async function(){
    try {
      const res = await fetch("{RAW_URL}", { method: 'GET', mode: 'cors', cache: 'no-store' });
      const headers = {};
      for (const pair of res.headers.entries()) headers[pair[0]] = pair[1];
      const info = {{
        ok: res.ok,
        status: res.status,
        statusText: res.statusText,
        url: res.url,
        headers: headers
      }};
      fetchInfo.innerText = JSON.stringify(info, null, 2);
    } catch (err) {
      fetchInfo.innerText = "FETCH ERROR: " + err.toString();
    }
  })();

  // CSS background applied?
  setTimeout(function(){
    const bgPreview = document.getElementById('bgPreview');
    const cs = window.getComputedStyle(bgPreview);
    const bg = cs.backgroundImage || cs.background;
    bgInfo.innerText = 'Computed background-image: ' + (bg || '(none)');
  }, 800);
})();
</script>
"""

# Inject HTML safely
components.html(html_code, height=400, scrolling=True)

st.markdown("---")
st.write("Paste the results below when ready.")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

st.title("DEBUG: Sidebar background image diagnostic (run once)")

st.markdown("**Instructions:** Reload the page, wait ~3s for tests to finish. Copy the text results below and paste them back here (or screenshot).")

# 1) Show the URL
st.write("Testing image URL:", RAW_URL)

# --- MAIN HTML (fully enclosed inside triple quotes!) ---
html_code = f"""
<div style="display:flex;gap:18px;align-items:flex-start;">
  <div>
    <div style="font-weight:700;margin-bottom:6px;">Direct &lt;img&gt; test</div>
    <img id="testImg" src="{RAW_URL}" style="max-width:320px; border: 2px solid #222; box-shadow: 0 6px 18px rgba(0,0,0,0.4);" />
    <div id="imgInfo" style="margin-top:8px;color:#ddd;font-family:monospace;"></div>
  </div>

  <div>
    <div style="font-weight:700;margin-bottom:6px;">CSS background test (sidebar preview)</div>
    <div id="bgPreview" style="width:320px;height:240px;border:2px solid #222;background:url('{RAW_URL}') center/cover no-repeat;"></div>
    <div id="bgInfo" style="margin-top:8px;color:#ddd;font-family:monospace;"></div>
  </div>

  <div style="min-width:300px;">
    <div style="font-weight:700;margin-bottom:6px;">Fetch/CORS test (JavaScript)</div>
    <pre id="fetchInfo" style="background:#071018;color:#9fe9c7;padding:10px;border-radius:6px;min-height:120px;overflow:auto;font-family:monospace;"></pre>
  </div>
</div>

<script>
(function(){
  const testImg = document.getElementById('testImg');
  const imgInfo = document.getElementById('imgInfo');
  const fetchInfo = document.getElementById('fetchInfo');
  const bgInfo = document.getElementById('bgInfo');

  // IMG load check
  testImg.onload = function(){
    imgInfo.innerText = 'IMG LOAD OK — naturalW x naturalH = ' +
      this.naturalWidth + ' x ' + this.naturalHeight;
  };
  testImg.onerror = function(){
    imgInfo.innerText = 'IMG LOAD ERROR — network or 404 or CORS issue';
  };

  // Fetch test
  (async function(){
    try {
      const res = await fetch("{RAW_URL}", { method: 'GET', mode: 'cors', cache: 'no-store' });
      const headers = {};
      for (const pair of res.headers.entries()) headers[pair[0]] = pair[1];
      const info = {{
        ok: res.ok,
        status: res.status,
        statusText: res.statusText,
        url: res.url,
        headers: headers
      }};
      fetchInfo.innerText = JSON.stringify(info, null, 2);
    } catch (err) {
      fetchInfo.innerText = "FETCH ERROR: " + err.toString();
    }
  })();

  // CSS background applied?
  setTimeout(function(){
    const bgPreview = document.getElementById('bgPreview');
    const cs = window.getComputedStyle(bgPreview);
    const bg = cs.backgroundImage || cs.background;
    bgInfo.innerText = 'Computed background-image: ' + (bg || '(none)');
  }, 800);
})();
</script>
"""

# Inject HTML safely
components.html(html_code, height=400, scrolling=True)

st.markdown("---")
st.write("Paste the results below when ready.")
