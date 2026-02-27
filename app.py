import streamlit as st
import pikepdf
import io
import pdfcrack
import qpdf

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CSS (NO CHANGES) ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #1e213a 0%, #050505 100%); color: #ffffff; }
    .header-box { text-align: center; padding: 25px; background: rgba(255, 255, 255, 0.05); border-radius: 20px; border: 1px solid rgba(212, 175, 55, 0.4); margin-bottom: 30px; }
    .main-title { font-size: 40px; font-weight: 900; letter-spacing: 5px; color: #d4af37; }
    .rgb-container { padding: 12px; border-radius: 10px; margin-bottom: 15px; background: rgba(0, 0, 0, 0.8); border: 2px solid transparent; text-align: center; font-weight: bold; animation: rgb-border 4s linear infinite; }
    @keyframes rgb-border { 0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; } 33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; color: #00ff00; } 66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; color: #0000ff; } 100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; } }
    div[data-testid="stRadio"] label { color: #FFFF00 !important; font-size: 22px !important; font-weight: 900 !important; }
    div[data-testid="stRadio"] p { color: #FFFFFF !important; font-size: 18px !important; font-weight: bold !important; }
    .stTextInput input { color: #FF0000 !important; background-color: rgba(255, 255, 255, 0.1) !important; border: 2px solid #FF0000 !important; font-size: 24px !important; font-weight: 900 !important; }
    div.stButton > button:first-child { background: linear-gradient(90deg, #FF1493 0%, #00BFFF 100%) !important; color: white !important; font-weight: 900 !important; font-size: 22px !important; border-radius: 12px !important; padding: 15px 0 !important; width: 100% !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="header-box"><p class="main-title">ULTRA RECOVERY</p><p style="color: #ffffff; font-size: 16px; margin-top:5px;">💎 Managed by: <span style="color: #d4af37; font-weight:bold;">VIKAS MISHRA</span></p></div>', unsafe_allow_html=True)

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

if uploaded_file and st.button("🚀 EXECUTE RECOVERY ENGINE"):
    pdf_bytes = uploaded_file.read()
    found = False
    status_box = st.empty()
    
    try:
        # Search List Taiyar Karna
        search_list = []
        if custom_hint:
            search_list.extend([custom_hint.lower(), custom_hint.upper()])
        else:
            search_list = ["vika", "VIKA", "mahe", "MAHE", "shre", "SHRE"] # Common names
        
        # --- CRACKING ENGINE ---
        for prefix in search_list:
            status_box.markdown(f"📡 **Scanning:** `{prefix}XXXX`...")
            for n in range(10000):
                password = f"{prefix}{n:04d}"
                try:
                    # Step 1: Open attempt
                    with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                        # 🔥 STEP 2: DEEP VERIFICATION (Save check) 🔥
                        # Agar yahan error nahi aaya, matlab password 100% sahi hai
                        unlocked_io = io.BytesIO()
                        pdf.save(unlocked_io)
                        
                        st.balloons()
                        st.success(f"🔓 VERIFIED FOUND: {password}")
                        st.download_button("📥 DOWNLOAD PDF", unlocked_io.getvalue(), f"Unlocked_{password}.pdf")
                        found = True
                        break
                except: continue
            if found: break

        if not found: st.error("❌ Password not found. Please check hint.")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
