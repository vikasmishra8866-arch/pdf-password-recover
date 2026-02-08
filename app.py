import streamlit as st
import pikepdf
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CSS FOR FULL VISIBILITY ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle, #1e213a 0%, #050505 100%);
        color: #ffffff;
    }
    
    /* Header Styling */
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

    /* RGB Boxes */
    .rgb-container {
        padding: 12px; border-radius: 10px; margin-bottom: 15px;
        background: rgba(0, 0, 0, 0.8); border: 2px solid transparent;
        text-align: center; font-weight: bold; text-transform: uppercase;
        animation: rgb-border 4s linear infinite;
    }

    @keyframes rgb-border {
        0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; color: #00ff00; }
        66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; color: #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; color: #ff0000; }
    }

    /* 🔥 FIX: RADIO BUTTON TEXT VISIBILITY 🔥 */
    /* Isse aapka 'Name' aur '8-Digit' wala text White dikhega */
    [data-testid="stWidgetLabel"] p {
        color: #FFFFFF !important;
        font-size: 20px !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px black;
    }
    
    .stRadio label {
        color: #FFFFFF !important; /* Pure White Labels */
        font-size: 18px !important;
        font-weight: 600 !important;
    }

    /* 🔥 FIX: INPUT HINT TEXT VISIBILITY 🔥 */
    .stTextInput input {
        color: #00FF00 !important; /* Neon Green/Yellow for typing */
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid #d4af37 !important;
        font-size: 22px !important;
        font-weight: 900 !important;
        border-radius: 10px !important;
    }

    /* Pink-Blue Button */
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
recovery_mode = st.radio("CHOOSE PATTERN:", ["Name + 4 Digits", "8-Digit Numbers Only"], horizontal=True)

st.markdown("---")

# --- UI INTERFACE ---
st.markdown('<div class="rgb-container">🛰️ Satellite Scanner Active</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

custom_hint = ""
if recovery_mode == "Name + 4 Digits":
    st.markdown('<div class="rgb-container">💡 Hint Engine Standby</div>', unsafe_allow_html=True)
    custom_hint = st.text_input("type_here", placeholder="Type name hint...", label_visibility="collapsed").upper().strip()

# --- DATABASE ---
COMMON_NAMES = ["AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU", "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE", "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA", "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM", "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI", "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI", "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE", "KUMA", "SING", "MISH", "SHAR", "VERM", "GUPT", "YADA", "PATE"]

if uploaded_file and st.button("🚀 EXECUTE RECOVERY ENGINE"):
    pdf_bytes = uploaded_file.read()
    found = False
    status_box = st.empty()
    
    try:
        if recovery_mode == "Name + 4 Digits":
            search_list = []
            if custom_hint and len(custom_hint) >= 4:
                for i in range(len(custom_hint) - 3): search_list.append(custom_hint[i:i+4])
            for name in COMMON_NAMES:
                if name not in search_list: search_list.append(name)
            
            bar = st.progress(0)
            for idx, prefix in enumerate(search_list):
                status_box.markdown(f"📡 **Scanning:** `{prefix}XXXX`...")
                bar.progress((idx + 1) / len(search_list))
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.balloons(); st.success(f"🔓 FOUND: {password}"); found = True
                            st.download_button("📥 DOWNLOAD", pdf_bytes, "unlocked.pdf"); break
                    except: continue
                if found: break

        else: # 8-Digit Numbers Mode
            status_box.warning("📡 Scanning 00000000 - 99999999. Please wait...")
            for n in range(100000000):
                password = f"{n:08d}"
                if n % 2000 == 0: status_box.markdown(f"📡 **Testing:** `{password}`...")
                try:
                    with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                        st.balloons(); st.success(f"🔓 FOUND: {password}"); found = True
                        st.download_button("📥 DOWNLOAD", pdf_bytes, "unlocked.pdf"); break
                except: continue
                if found: break

        if not found: st.error("❌ Password not found.")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
