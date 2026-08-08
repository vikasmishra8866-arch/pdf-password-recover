import streamlit as st
import streamlit.components.v1 as components
import pikepdf
import io
import time
import base64
import json
import re

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Vikas Mishra | Ultra Recovery Pro",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DICTIONARY FOR FAST BRUTEFORCE ---
COMMON_NAMES = [
    "AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU", 
    "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE", 
    "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA", 
    "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM", 
    "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI", 
    "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI", 
    "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE", 
    "KUMA", "SING", "MISH", "SHAR", "VERM", "GUPT", "YADA", "PATE", "CHAU", "KHAN"
]

# --- HIDE STREAMLIT CHROME ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background: #031329 !important; padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { width: 100% !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

# --- BACKEND RECOVERY ENGINE ---
def process_pdf_recovery(pdf_bytes, mode, hint):
    start_time = time.time()
    found_password = None
    unlocked_bytes = None

    if mode == "name_digits":
        search_prefixes = []
        hint = re.sub(r'[^A-Z0-9]', '', hint.upper())
        if len(hint) >= 4:
            for i in range(len(hint) - 3):
                search_prefixes.append(hint[i:i+4])
        
        search_prefixes.extend(COMMON_NAMES)
        search_prefixes = list(dict.fromkeys(search_prefixes))

        for prefix in search_prefixes:
            for n in range(10000):
                test_pass = f"{prefix}{n:04d}"
                try:
                    with pikepdf.open(io.BytesIO(pdf_bytes), password=test_pass) as pdf:
                        out_stream = io.BytesIO()
                        pdf.save(out_stream)
                        found_password = test_pass
                        unlocked_bytes = out_stream.getvalue()
                        break
                except:
                    continue
            if found_password:
                break

    else: # Numeric 8-Digit
        for n in range(100000000):
            test_pass = f"{n:08d}"
            try:
                with pikepdf.open(io.BytesIO(pdf_bytes), password=test_pass) as pdf:
                    out_stream = io.BytesIO()
                    pdf.save(out_stream)
                    found_password = test_pass
                    unlocked_bytes = out_stream.getvalue()
                    break
            except:
                continue

    elapsed = round(time.time() - start_time, 2)
    return found_password, unlocked_bytes, elapsed


# --- PURE PREMIUM HTML + TAILWIND FRONTEND UI ---
HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@500;700&family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
  <style>
    body {
      background: radial-gradient(circle at 50% 0%, #0d284f 0%, #031329 85%);
      background-size: 200% 200%;
      animation: hydroPulse 10s ease infinite;
      color: #f8fafc;
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
      margin: 0;
    }
    @keyframes hydroPulse {
      0%, 100% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
    }
    .hydro-card {
      background: #0b1d3a;
      border: 1px solid rgba(6, 182, 212, 0.3);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
      border-radius: 20px;
      backdrop-filter: blur(10px);
      transition: all 0.3s ease;
    }
    .hydro-card:hover {
      border-color: #06b6d4;
      box-shadow: 0 0 25px rgba(6, 182, 212, 0.25);
    }
    .cyber-input {
      background: rgba(3, 19, 41, 0.9);
      border: 1px solid rgba(6, 182, 212, 0.4);
      color: #38bdf8;
      font-weight: 800;
      letter-spacing: 2px;
      transition: all 0.2s ease;
    }
    .cyber-input:focus {
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }
    .btn-cyber {
      background: linear-gradient(135deg, #06b6d4 0%, #0284c7 100%);
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
      transition: all 0.25s ease;
    }
    .btn-cyber:hover:not(:disabled) {
      transform: translateY(-2px) scale(1.01);
      box-shadow: 0 0 30px rgba(6, 182, 212, 0.8);
    }
    .btn-cyber:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    .tv-terminal {
      background: #020b14;
      border: 2px solid #06b6d4;
      box-shadow: inset 0 0 15px rgba(6, 182, 212, 0.3);
      border-radius: 14px;
      font-family: 'Fira Code', monospace;
      color: #00ff66;
    }
  </style>
</head>
<body>

  <div class="w-full max-w-xl space-y-5">
    
    <!-- HEADER -->
    <div class="hydro-card p-6 text-center">
      <h1 class="text-3xl font-black tracking-widest text-amber-400 drop-shadow-md">
        ULTRA RECOVERY PRO
      </h1>
      <p class="text-xs text-slate-400 mt-2 font-semibold">
        💎 Managed by: <span class="text-amber-400 font-bold">VIKAS MISHRA</span>
      </p>
    </div>

    <!-- MAIN FORM -->
    <div class="hydro-card p-6 space-y-5">
      
      <!-- MODE SELECT -->
      <div>
        <label class="text-xs font-bold text-cyan-400 uppercase tracking-widest block mb-2">
          ⚙️ RECOVERY MODE SELECTION
        </label>
        <div class="grid grid-cols-2 gap-3">
          <button id="mode1" onclick="selectMode('name_digits')" class="py-3 px-4 rounded-xl text-xs font-bold bg-cyan-500/20 border border-cyan-400 text-cyan-300">
            Name + 4 Digits
          </button>
          <button id="mode2" onclick="selectMode('numeric_8')" class="py-3 px-4 rounded-xl text-xs font-bold bg-slate-900 border border-slate-700 text-slate-400">
            8-Digit Numbers
          </button>
        </div>
      </div>

      <!-- DROPZONE -->
      <div>
        <label class="text-xs font-bold text-cyan-400 uppercase tracking-widest block mb-2">
          📄 UPLOAD ENCRYPTED PDF
        </label>
        <div onclick="document.getElementById('pdfInput').click()" class="border-2 border-dashed border-cyan-500/40 rounded-xl p-6 text-center bg-cyan-950/20 cursor-pointer hover:border-cyan-400 transition">
          <i class="fa-solid fa-cloud-arrow-up text-3xl text-cyan-400 mb-2"></i>
          <p id="fileLabel" class="text-xs text-slate-300 font-semibold">Click or Drag PDF file here</p>
          <input type="file" id="pdfInput" accept="application/pdf" class="hidden" onchange="fileSelected(event)">
        </div>
      </div>

      <!-- HINT INPUT -->
      <div id="hintBox">
        <label class="text-xs font-bold text-cyan-400 uppercase tracking-widest block mb-2">
          💡 NAME HINT
        </label>
        <input 
          type="text" 
          id="nameHint" 
          placeholder="TYPE NAME HINT (E.G. VIKAS)" 
          class="cyber-input w-full px-4 py-3 rounded-xl text-sm uppercase"
          oninput="this.value = this.value.replace(/[^a-zA-Z0-9]/g, '').toUpperCase()"
        >
      </div>

      <!-- EXECUTE BUTTON -->
      <button id="execBtn" onclick="startRecovery()" class="btn-cyber w-full py-4 rounded-xl text-white font-black text-sm tracking-wider flex items-center justify-center gap-2">
        <i class="fa-solid fa-bolt text-amber-300"></i>
        <span>EXECUTE RECOVERY ENGINE</span>
      </button>

    </div>

    <!-- HACKER TERMINAL -->
    <div id="terminal" class="hydro-card p-4 space-y-2 hidden">
      <div class="flex justify-between items-center text-xs text-cyan-400 font-mono">
        <span><i class="fa-solid fa-terminal"></i> ENGINE STATUS</span>
        <span class="animate-pulse text-emerald-400">● PROCESSING</span>
      </div>
      <div class="tv-terminal p-4 text-xs space-y-1" id="logs">
        <div>> [SYSTEM_INIT] Booting C++ Decryption Engine...</div>
      </div>
    </div>

  </div>

  <script>
    let currentMode = 'name_digits';
    let base64PDF = null;

    function selectMode(m) {
      currentMode = m;
      if(m === 'name_digits') {
        document.getElementById('mode1').className = "py-3 px-4 rounded-xl text-xs font-bold bg-cyan-500/20 border border-cyan-400 text-cyan-300";
        document.getElementById('mode2').className = "py-3 px-4 rounded-xl text-xs font-bold bg-slate-900 border border-slate-700 text-slate-400";
        document.getElementById('hintBox').style.display = 'block';
      } else {
        document.getElementById('mode2').className = "py-3 px-4 rounded-xl text-xs font-bold bg-cyan-500/20 border border-cyan-400 text-cyan-300";
        document.getElementById('mode1').className = "py-3 px-4 rounded-xl text-xs font-bold bg-slate-900 border border-slate-700 text-slate-400";
        document.getElementById('hintBox').style.display = 'none';
      }
    }

    function fileSelected(e) {
      const file = e.target.files[0];
      if(file) {
        document.getElementById('fileLabel').innerText = file.name;
        document.getElementById('fileLabel').classList.add('text-amber-300');
        const reader = new FileReader();
        reader.onload = function(evt) {
          base64PDF = evt.target.result.split(',')[1];
        };
        reader.readAsDataURL(file);
      }
    }

    function startRecovery() {
      if(!base64PDF) {
        alert("Please upload a PDF file first!");
        return;
      }
      
      document.getElementById('terminal').classList.remove('hidden');
      const logs = document.getElementById('logs');
      logs.innerHTML = "<div>> [SYSTEM_INIT] Booting C++ Decryption Engine...</div><div>> Scanning Decryption Matrix...</div>";

      // Send payload to Streamlit
      const payload = {
        pdf: base64PDF,
        mode: currentMode,
        hint: document.getElementById('nameHint').value
      };

      window.parent.postMessage({
        type: "streamlit:setComponentValue",
        value: JSON.stringify(payload)
      }, "*");
    }
  </script>
</body>
</html>
"""

# Render UI using Component
data_from_ui = components.html(HTML_FRONTEND, height=720, scrolling=False)

# When user submits from UI
if data_from_ui:
    try:
        payload = json.loads(data_from_ui)
        pdf_bytes = base64.b64decode(payload['pdf'])
        mode = payload['mode']
        hint = payload['hint']

        with st.spinner("Decrypting..."):
            password, unlocked_bytes, elapsed = process_pdf_recovery(pdf_bytes, mode, hint)

        if password:
            st.balloons()
            st.success(f"🔓 UNLOCKED! Password: {password} (Time: {elapsed}s)")
            st.download_button(
                label="📥 DOWNLOAD UNLOCKED PDF",
                data=unlocked_bytes,
                file_name=f"Unlocked_{password}.pdf",
                mime="application/pdf"
            )
        else:
            st.error("❌ Password not found in standard dictionary. Try a different hint.")
    except Exception as e:
        st.error(f"Error: {e}")
