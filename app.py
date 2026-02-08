import streamlit as st
import pikepdf
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Recovery", page_icon="🔑", layout="centered")

# --- CUSTOM CLEAN PREMIUM CSS ---
st.markdown("""
    <style>
    /* Main Background - Deep Charcoal Black */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Header Section */
    .header-container {
        text-align: center;
        padding: 40px 0px;
        background: linear-gradient(to bottom, #1a1c23, #0e1117);
        border-bottom: 2px solid #d4af37;
        margin-bottom: 30px;
        border-radius: 0px 0px 30px 30px;
    }
    
    .main-title {
        font-size: 38px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #d4af37; /* Gold Color */
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    
    .sub-title {
        font-size: 16px;
        color: #888;
        font-style: italic;
    }

    /* Glass Cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stFileUploader) {
        background: #161b22;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #30363d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Input Field Styling */
    .stTextInput input {
        border-radius: 10px !important;
        border: 1px solid #30363d !important;
        background-color: #0d1117 !important;
        color: gold !important;
        height: 50px;
    }

    /* Premium Button */
    div.stButton > button:first-child {
        background: #d4af37;
        color: #000;
        border: none;
        padding: 12px 0px;
        font-weight: 800;
        font-size: 18px;
        border-radius: 12px;
        width: 100%;
        transition: 0.4s;
        text-transform: uppercase;
        margin-top: 20px;
    }
    
    div.stButton > button:first-child:hover {
        background: #f4cf57;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
        transform: scale(1.02);
    }

    /* Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-container">
        <p class="main-title">PDF PASS RECOVERY</p>
        <p class="sub-title">SECURE • FAST • RELIABLE</p>
        <p style="color: #d4af37; font-weight: bold;">💎 Managed by: VIKAS MISHRA</p>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN SYSTEM ---
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

# UI Layout
st.write("### 📂 Upload Locked File")
uploaded_file = st.file_uploader("", type=["pdf"])

st.write("### 🔍 Recovery Hint (Optional)")
custom_hint = st.text_input("", placeholder="Enter Name or Hint (e.g. VIKA)").upper().strip()

if uploaded_file:
    if st.button("RUN RECOVERY ENGINE"):
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
                status_box.markdown(f"📡 **Searching Pattern:** `{prefix}XXXX` ({idx+1}/{total})")
                bar.progress((idx + 1) / total)
                
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.balloons()
                            st.success(f"🔓 PASSWORD FOUND: {password}")
                            
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 DOWNLOAD DECRYPTED PDF", out_buf.getvalue(), "unlocked.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break
            
            if not found:
                st.error("❌ Pattern not found in our database.")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<br><hr><center style='color:#555;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
