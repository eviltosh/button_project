# DIAGNOSTIC base.py — paste/overwrite and run on Streamlit Cloud
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

st.title("DEBUG: Sidebar background image diagnostic (run once)")

st.markdown("**Instructions:** Reload the page, wait ~3s for tests to finish. Copy the text results below and paste them back here (or screenshot).")

# 1) Show the URL we're testing
st.write("Testing image URL:", RAW_URL)

# 2) Show an <img> tag (simple browser-level test)
img_html = f"""
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

  // img load / error handlers
  testImg.onload = function(){
    imgInfo.innerText = 'IMG LOAD OK — naturalW x naturalH = ' + this.naturalWidth + ' x ' + this.naturalHeight;
  };
  testImg.onerror = function(ev){
    imgInfo.innerText = 'IMG LOAD ERROR — network or 404 or CORS blocking the resource';
  };

  // Fetch test to inspect status & headers
  (async function(){
    try {
      const res = await fetch("{RAW_URL}", { method: 'GET', mode: 'cors', cache: 'no-store' });
      const headers = {};
      for (const pair of res.headers.entries()) headers[pair[0]] = pair[1];
      const info = {
        ok: res.ok,
        status: res.status,
        statusText: res.statusText,
        url: res.url,
        headers: headers
      };
      fetchInfo.innerText = JSON.stringify(info, null, 2);
      if (!res.ok) {
          try {
              const txt = await res.text();
              fetchInfo.innerText += "\\n\\n=== response text (first 500 chars) ===\\n" + txt.slice(0,500);
          } catch(e){}
      }
    } catch (err) {
      fetchInfo.innerText = "FETCH ERROR — likely CORS or network blocked:\\n" + err.toString();
    }
  })();

  setTimeout(function(){
    const bgPreview = document.getElementById('bgPreview');
    const cs = window.getComputedStyle(bgPreview);
    const bg = cs.backgroundImage || cs.background;
    bgInfo.innerText = 'Computed background-image: ' + (bg || '(none)');
  }, 800);
})();
</script>
"""

components.html(img_html, height=380, scrolling=True)

st.markdown("---")
st.write("After the tests finish, paste the **three** results from the page here (or screenshot):")
st.write("- The `IMG LOAD` line under the image") 
st.write("- The `Fetch/CORS test` JSON output (or error text)") 
st.write("- The `Computed background-image` line under the preview")

st.write("If the fetch status shows `status: 200` and the image still doesn’t appear as the sidebar background, paste the fetch JSON and I will produce the final working fallback.")
