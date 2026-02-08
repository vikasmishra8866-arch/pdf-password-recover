import streamlit as st
import pikepdf
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CSS FOR RGB NEON & GLOSSY BOXES ---
st.markdown("""
    <style>
    /* 1. Background Visibility Fix */
    .stApp {
        background: linear-gradient(135deg, #1a1c2c 0%, #4a192c 100%);
        color: #ffffff;
    }
    
    /* 2. Premium Header with Gold Glow */
    .header-box {
        text-align: center;
        padding: 30px;
        background: rgba(255, 255, 255, 0.07);
        border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        margin-bottom: 40px;
        backdrop-filter: blur(10px);
    }
    
    .main-title {
        font-size: 45px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #d4af37;
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
        margin: 0;
    }

    /* 3. RGB ANIMATED GLOSSY BOXES */
    .rgb-box {
        background: rgba(0, 0, 0, 0.5) !important;
        padding: 25px;
        border-radius: 15px;
        position: relative;
        margin-bottom: 30px;
        backdrop-filter: blur(20px);
        border: 2px solid transparent;
        background-clip: padding-box;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }
    
    /* RGB Border Animation Logic */
    @keyframes rgb-animation {
        0% { border-color: #ff0000; box-shadow: 0 0 15px #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 15px #00ff00; }
        66% { border-color: #0000ff; box-shadow: 0 0 15px #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 15px #ff0000; }
    }

    .rgb-box {
        animation: rgb-animation 5s linear infinite;
    }

    /* 4. Glossy Input Fields */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        padding: 12px !important;
        transition: 0.3s;
    }
    
    .stTextInput input:focus {
        border-color: #d4af37 !important;
        background: rgba(255, 255, 255, 0.2) !important;
    }

    /* 5. Execution Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
        background-size: 400%;
        color: white !important;
        border: none;
        font-weight: 800;
        font-size: 22px;
        border-radius: 15px;
        padding: 18px 0;
        width: 100%;
        animation: rgb-animation 20s linear infinite;
        transition: 0.5s;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.03);
        filter: brightness(1.2);
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

# --- NAMES DATA ---
COMMON_NAMES = ["AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU", "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE", "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA", "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM", "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI", "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI", "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE"]

# --- RGB INTERFACE BOXES ---
st.markdown('<div class="rgb-box">', unsafe_allow_html=True)
st.write("### 📂 1. Select Locked PDF")
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="rgb-box">', unsafe_allow_html=True)
st.write("### 🔍 2. Enter Hint (4 Letters)")
custom_hint = st.text_input("", placeholder="Hint: e.g. VIKA", label_visibility="collapsed").upper().strip()
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
                status_box.markdown(f"📡 **Scanning:** `{prefix}XXXX`...")
                bar.progress((idx + 1) / len(search_list))
                
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.balloons()
                            st.success(f"🔓 PASSWORD FOUND: {password}")
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 DOWNLOAD PDF", out_buf.getvalue(), "decrypted.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<br><center style='color:#bbb;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
