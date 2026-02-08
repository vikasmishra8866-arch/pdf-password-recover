import streamlit as st
import pikepdf
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CSS FOR NEON LIGHTING & GLOSSY FINISH ---
st.markdown("""
    <style>
    /* Main Background with better visibility */
    .stApp {
        background: radial-gradient(circle, #1b2735 0%, #090a0f 100%);
        color: #ffffff;
    }
    
    /* Premium Header */
    .header-box {
        text-align: center;
        padding: 30px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .main-title {
        font-size: 42px;
        font-weight: 850;
        letter-spacing: 3px;
        color: #d4af37;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
        margin: 0;
    }

    /* NEON LIGHTING BOXES */
    .glow-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
        backdrop-filter: blur(15px);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1);
    }
    
    /* Border Animation Effect */
    .glow-box::after {
        content: '';
        position: absolute;
        top: -2px; left: -2px; right: -2px; bottom: -2px;
        background: linear-gradient(45deg, #d4af37, #ffffff, #d4af37);
        z-index: -1;
        filter: blur(5px);
        animation: border-glow 4s linear infinite;
        border-radius: 17px;
        opacity: 0.6;
    }

    @keyframes border-glow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }

    /* Glossy Inputs */
    .stTextInput input {
        background: rgba(0, 0, 0, 0.4) !important;
        border: 1px solid #d4af37 !important;
        color: #ffffff !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Premium Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #d4af37 0%, #f4cf57 100%);
        color: #000 !important;
        border: none;
        font-weight: 900;
        font-size: 20px;
        letter-spacing: 1px;
        border-radius: 12px;
        padding: 15px 0;
        width: 100%;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
        transition: 0.4s ease;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.7);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div class="header-box">
        <p class="main-title">ULTRA RECOVERY</p>
        <p style="color: #ffffff; font-size: 18px; margin-top:10px;">
            💎 Managed by: <span style="color: #d4af37; font-weight:bold;">VIKAS MISHRA</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- COMMON NAMES DATA ---
COMMON_NAMES = [
    "AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU",
    "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE",
    "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA",
    "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM",
    "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI",
    "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI",
    "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE"
]

# --- MAIN INTERFACE ---
st.markdown('<div class="glow-box">', unsafe_allow_html=True)
st.write("### 📂 1. Select Locked PDF")
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glow-box">', unsafe_allow_html=True)
st.write("### 🔍 2. Enter Hint (4 Letters)")
custom_hint = st.text_input("", placeholder="Example: VIKA or SHYA", label_visibility="collapsed").upper().strip()
st.markdown('</div>', unsafe_allow_html=True)

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
                status_box.markdown(f"📡 **Status:** Testing `{prefix}XXXX` pattern...")
                bar.progress((idx + 1) / len(search_list))
                
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.balloons()
                            st.success(f"🔓 SUCCESS! Password is: {password}")
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 DOWNLOAD UNLOCKED FILE", out_buf.getvalue(), "decrypted.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break
            
            if not found:
                st.error("❌ Could not recover password with current patterns.")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<br><center style='color:#777; font-size:12px;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
