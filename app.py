import streamlit as st
import pikepdf
import io
import subprocess
import os
import re

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1e213a 0%, #050505 100%);
        color: #ffffff;
    }
    .header-box {
        text-align: center;
        padding: 25px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.4);
        margin-bottom: 30px;
    }
    .main-title {
        font-size: 40px; font-weight: 900; letter-spacing: 5px; color: #d4af37;
    }
    .rgb-container {
        padding: 12px; border-radius: 10px; margin-bottom: 15px;
        background: rgba(0, 0, 0, 0.8); border: 2px solid transparent;
        text-align: center; font-weight: bold; animation: rgb-border 4s linear infinite;
    }
    @keyframes rgb-border {
        0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; color: #00ff00; }
        66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; color: #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; }
    }
    div[data-testid="stRadio"] label {
        color: #FFFF00 !important; 
        font-size: 22px !important;
        font-weight: 900 !important;
        cursor: pointer;
    }
    div[data-testid="stRadio"] p {
        color: #FFFFFF !important; 
        font-size: 18px !important;
        font-weight: bold !important;
    }
    .stTextInput input {
        color: #FF0000 !important; 
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid #FF0000 !important; 
        font-size: 24px !important;
        font-weight: 900 !important;
        text-shadow: 0 0 8px rgba(255, 0, 0, 0.6); 
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #FF1493 0%, #00BFFF 100%) !important;
        color: white !important; border: none !important; font-weight: 900 !important;
        font-size: 22px !important; border-radius: 12px !important; padding: 15px 0 !important;
        width: 100% !important; box-shadow: 0 5px 15px rgba(255, 20, 147, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-box">
        <p class="main-title">ULTRA RECOVERY</p>
        <p style="color: #ffffff; font-size: 16px; margin-top:5px;">
            💎 Managed by: <span style="color: #d4af37; font-weight:bold;">VIKAS MISHRA</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- MODE SELECTION ---
st.markdown('<div class="rgb-container">⚙️ RECOVERY MODE SELECTION</div>', unsafe_allow_html=True)
recovery_mode = st.radio("CHOOSE SCANNING PATTERN:", ["Name + 4 Digits", "8-Digit Numbers Only"], horizontal=True)

st.markdown("---")

# --- UI INTERFACE ---
st.markdown('<div class="rgb-container">🛰️ Satellite Scanner Active</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

custom_hint = ""
if recovery_mode == "Name + 4 Digits":
    st.markdown('<div class="rgb-container">💡 Hint Engine Standby</div>', unsafe_allow_html=True)
    custom_hint = st.text_input("type_here", placeholder="Type name hint (e.g. Vikas)", label_visibility="collapsed").strip()

# --- EXPANDED DATABASE ---
COMMON_NAMES = ["AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "VIKA", "MAHE", "SHRE"]

if uploaded_file and st.button("🚀 EXECUTE RECOVERY ENGINE"):
    # File save for PDFCrack
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    found = False
    status_box = st.empty()
    
    try:
        # 1. Building Wordlist for accuracy
        status_box.info("📝 Building smart wordlist...")
        with open("mypass.txt", "w") as f:
            if recovery_mode == "Name + 4 Digits":
                search_prefixes = [custom_hint] if custom_hint else COMMON_NAMES
                for prefix in search_prefixes:
                    if len(prefix) >= 4:
                        prefix = prefix[:4]
                        for i in range(10000):
                            f.write(f"{prefix.lower()}{i:04d}\n")
                            f.write(f"{prefix.upper()}{i:04d}\n")
            else:
                for i in range(100000000):
                    f.write(f"{i:08d}\n")

        # 2. RUNNING PDFCRACK (Direct Ubuntu Engine)
        status_box.markdown('<div class="rgb-container">📡 SYSTEM CORE CRACKING ACTIVE...</div>', unsafe_allow_html=True)
        
        # Calling PDFCrack directly
        cmd = "pdfcrack -f temp.pdf -w mypass.txt"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True)
        stdout, _ = process.communicate()
        
        # 3. VERIFYING RESULT
        match = re.search(r"found user-password: (.+)", stdout)
        if match:
            password = match.group(1).strip()
            # Strict cleaning
            final_pass = re.sub(r'[^a-zA-Z0-9]', '', password)
            
            st.balloons()
            st.success(f"🔓 VERIFIED FOUND: {final_pass}")
            
            # Using pikepdf only to save the file for user
            with pikepdf.open("temp.pdf", password=final_pass) as pdf:
                out = io.BytesIO()
                pdf.save(out)
                st.download_button("📥 DOWNLOAD UNLOCKED PDF", out.getvalue(), f"Unlocked_{final_pass}.pdf")
            found = True
        else:
            st.error("❌ Password not found. Please check your hint.")

    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        # Cleanup
        if os.path.exists("temp.pdf"): os.remove("temp.pdf")
        if os.path.exists("mypass.txt"): os.remove("mypass.txt")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
