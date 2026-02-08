import streamlit as st
import pikepdf
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Pawan PDF Unlocker Pro", page_icon="🔓", layout="wide")

# --- CUSTOM PREMIUM CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    
    /* Header Style */
    .main-title {
        font-size: 45px;
        font-weight: 800;
        color: #00d2ff;
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,210,255,0.3);
        margin-bottom: 0px;
    }
    
    .managed-by {
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 5px 20px;
        border-radius: 50px;
        width: fit-content;
        margin: 0 auto 30px auto;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* Card/Box Style */
    .stFileUploader, .stTextInput, .stButton {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Button Animation */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        font-weight: bold;
        font-size: 20px;
        border-radius: 10px;
        transition: 0.3s all;
        box-shadow: 0 4px 15px rgba(0,210,255,0.4);
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(0,210,255,0.6);
        background: linear-gradient(90deg, #3a7bd5 0%, #00d2ff 100%);
    }

    /* Input Field Focus */
    .stTextInput input {
        color: white !important;
        background-color: rgba(0,0,0,0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<p class="main-title">🔓 PAWAN PDF RECOVERY PRO</p>', unsafe_allow_html=True)
st.markdown('<p class="managed-by">💎 Managed by: <b>VIKAS MISHRA</b></p>', unsafe_allow_html=True)

# --- APP LOGIC ---
COMMON_NAMES = [
    "AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU",
    "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE",
    "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA",
    "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM",
    "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI",
    "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI",
    "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE",
    "SURA", "KUMA", "SING", "YADA", "MISH", "SHAR", "VERM", "KHAN", "SAIN", "RAWA",
    "CHOU", "THAK", "GUPT", "KAPO", "MALH", "MEHT", "JOSH", "PATE", "DESA", "NAIR",
    "RAJE", "SURE", "MAHE", "NARE", "JITE", "MUKE", "KESH", "KAMA", "KANT", "SHRA"
]

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📥 1. Upload Document")
    uploaded_file = st.file_uploader("", type=["pdf"])

with col2:
    st.markdown("### 💡 2. Add Your Hint")
    custom_hint = st.text_input("", placeholder="Andaja wale 4 letters yahan likhein...").upper().strip()

st.markdown("---")

if uploaded_file:
    if st.button("🚀 START DEEP SCAN"):
        pdf_bytes = uploaded_file.read()
        found = False
        
        # Priority Logic
        search_list = []
        if custom_hint and len(custom_hint) >= 4:
            for i in range(len(custom_hint) - 3):
                search_list.append(custom_hint[i:i+4])
        
        for name in COMMON_NAMES:
            if name not in search_list:
                search_list.append(name)
        
        status_box = st.empty()
        bar = st.progress(0)
        
        total = len(search_list)
        
        try:
            for idx, prefix in enumerate(search_list):
                status_box.info(f"🔍 Testing Pattern: {prefix}XXXX ({idx+1}/{total})")
                bar.progress((idx + 1) / total)
                
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.balloons()
                            st.success(f"✅ FOUND IT! Password is: {password}")
                            
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 DOWNLOAD UNLOCKED PDF", out_buf.getvalue(), "unlocked.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break
            
            if not found:
                st.error("❌ Password nahi mila. Kripya dusri hint try karein.")
        except Exception as e:
            st.error(f"Technical Error: {e}")

st.markdown("<br><center>© 2026 PAWAN AUTO FINANCE - PREMIUM RECOVERY TOOLS</center>", unsafe_allow_html=True)
