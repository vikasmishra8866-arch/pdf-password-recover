import streamlit as st
import pikepdf
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CSS FOR RGB NEON, GLOSSY BOXES & ANIMATED TEXT ---
st.markdown("""
    <style>
    /* Main Background - High Visibility Dark Gradient */
    .stApp {
        background: radial-gradient(circle, #1e213a 0%, #050505 100%);
        color: #ffffff;
    }
    
    /* Premium Header */
    .header-box {
        text-align: center;
        padding: 25px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.4);
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    
    .main-title {
        font-size: 40px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #d4af37;
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
    }

    /* RGB ANIMATED BOXES WITH TEXT */
    .rgb-container {
        padding: 20px;
        border-radius: 15px;
        position: relative;
        margin-bottom: 25px;
        backdrop-filter: blur(15px);
        background: rgba(0, 0, 0, 0.6);
        border: 2px solid transparent;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        animation: rgb-border 4s linear infinite;
    }

    @keyframes rgb-border {
        0% { border-color: #ff0000; box-shadow: 0 0 15px #ff0000; color: #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 15px #00ff00; color: #00ff00; }
        66% { border-color: #0000ff; box-shadow: 0 0 15px #0000ff; color: #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 15px #ff0000; color: #ff0000; }
    }

    /* Glossy Inputs */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }

    /* RGB Execution Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
        background-size: 400%;
        color: white !important;
        border: none;
        font-weight: 900;
        font-size: 20px;
        border-radius: 12px;
        padding: 15px 0;
        width: 100%;
        animation: rainbow-button 10s linear infinite;
        box-shadow: 0 0 20px rgba(255,255,255,0.2);
    }

    @keyframes rainbow-button {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
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

# --- DATA ---
COMMON_NAMES = ["AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU", "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE", "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA", "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM", "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI", "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI", "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE"]

# --- UI INTERFACE ---

# 1. First RGB Box with Active Text
st.markdown('<div class="rgb-container">🛰️ Satellite Scanner Active</div>', unsafe_allow_html=True)
st.write("### 📂 1. Select Locked PDF")
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# 2. Second RGB Box with Instruction Text
st.markdown('<div class="rgb-container">💡 Hint Engine Standby</div>', unsafe_allow_html=True)
st.write("### 🔍 2. Enter Hint (4 Letters)")
custom_hint = st.text_input("", placeholder="Hint: e.g. VIKA", label_visibility="collapsed").upper().strip()

st.markdown("<br>", unsafe_allow_html=True)

if uploaded_file:
    if st.button("🚀 EXECUTE RECOVERY ENGINE"):
        pdf_bytes = uploaded_file.read()
        found = False
        
        search_list = []
        if custom_hint and len(custom_hint) >= 4:
            for i in range(len(custom_hint) - 3):
                search_list.append(custom_hint[i:i+4])
        
        for name in COMMON_NAMES:
            if name not in search_list:
                search_list.append(name)
        
        status_box = st.empty()
        bar = st.progress(0)
        
        try:
            for idx, prefix in enumerate(search_list):
                status_box.markdown(f"📡 **Scanning:** `{prefix}XXXX`...")
                bar.progress((idx + 1) / len(search_list))
                
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.balloons()
                            st.success(f"🔓 SUCCESS! Password is: {password}")
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 DOWNLOAD PDF", out_buf.getvalue(), "decrypted.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break
            if not found: st.error("❌ Pattern not found.")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<br><center style='color:#555; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
