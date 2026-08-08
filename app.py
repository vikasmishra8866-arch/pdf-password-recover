import streamlit as st
import pikepdf
import io
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | Ultra Recovery Pro", page_icon="🔑", layout="centered")

# --- CUSTOM CSS: DEEP OCEAN HYDRO & HACKER TV THEME ---
st.markdown("""
    <style>
    :root {
        --bg-ocean: #031329;
        --card-navy: #0b1d3a;
        --border-cyan: rgba(6, 182, 212, 0.25);
        --accent-cyan: #06b6d4;
        --cyan-light: #22d3ee;
        --gold-main: #f59e0b;
    }

    /* GLOBAL ANIMATED HYDRO BACKGROUND */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d284f 0%, #031329 85%) !important;
        background-size: 200% 200% !important;
        animation: hydroPulse 12s ease infinite !important;
        color: #f8fafc !important;
    }

    @keyframes hydroPulse {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    /* HEADER CONTAINER WITH HOVER SHADOW */
    .header-box {
        text-align: center;
        padding: 25px;
        background: #0b1d3a;
        border-radius: 20px;
        border: 1px solid rgba(245, 158, 11, 0.4);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
        transition: all 0.35s ease;
    }
    .header-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(245, 158, 11, 0.3);
        border-color: #f59e0b;
    }

    .main-title {
        font-size: 36px; font-weight: 900; letter-spacing: 4px; color: #f59e0b;
        margin: 0;
    }

    /* RGB NEON BORDER CONTAINER */
    .rgb-container {
        padding: 12px; border-radius: 12px; margin-bottom: 15px;
        background: rgba(0, 0, 0, 0.85); border: 2px solid transparent;
        text-align: center; font-weight: 800; letter-spacing: 1px;
        animation: rgb-border 4s linear infinite;
    }
    @keyframes rgb-border {
        0% { border-color: #ff0000; box-shadow: 0 0 12px #ff0000; color: #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 12px #00ff00; color: #00ff00; }
        66% { border-color: #00bfff; box-shadow: 0 0 12px #00bfff; color: #00bfff; }
        100% { border-color: #ff0000; box-shadow: 0 0 12px #ff0000; color: #ff0000; }
    }

    /* YELLOW TEXT FOR RADIO OPTIONS */
    div[data-testid="stRadio"] label {
        color: #FFFF00 !important; 
        font-size: 20px !important;
        font-weight: 900 !important;
        cursor: pointer;
    }
    div[data-testid="stRadio"] p {
        color: #FFFFFF !important; 
        font-size: 16px !important;
        font-weight: bold !important;
    }

    /* RED TEXT INPUT IN HINT ENGINE */
    .stTextInput input {
        color: #FF0000 !important; 
        background-color: rgba(3, 19, 41, 0.9) !important;
        border: 2px solid #FF0000 !important; 
        border-radius: 12px !important;
        font-size: 22px !important;
        font-weight: 900 !important;
        text-shadow: 0 0 8px rgba(255, 0, 0, 0.6); 
        text-transform: uppercase;
    }

    /* CYBER GLOW EXECUTION BUTTON */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #06b6d4 0%, #0284c7 100%) !important;
        color: white !important; border: none !important; font-weight: 900 !important;
        font-size: 20px !important; border-radius: 14px !important; padding: 15px 0 !important;
        width: 100% !important; box-shadow: 0 5px 20px rgba(6, 182, 212, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 10px 25px rgba(6, 182, 212, 0.6) !important;
    }

    /* HACKER TV TERMINAL DISPLAY */
    .tv-screen {
        background-color: #020b14;
        border: 3px solid #06b6d4;
        box-shadow: inset 0 0 15px rgba(6, 182, 212, 0.5), 0 0 20px rgba(6, 182, 212, 0.3);
        border-radius: 16px;
        padding: 18px;
        font-family: 'Courier New', Courier, monospace;
        color: #00ff66;
        text-shadow: 0 0 5px rgba(0, 255, 102, 0.8);
        margin-top: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div class="header-box">
        <p class="main-title">ULTRA RECOVERY PRO</p>
        <p style="color: #cbd5e1; font-size: 15px; margin-top:8px;">
            💎 Managed by: <span style="color: #f59e0b; font-weight:bold;">VIKAS MISHRA</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- MODE SELECTION ---
st.markdown('<div class="rgb-container">⚙️ RECOVERY MODE SELECTION</div>', unsafe_allow_html=True)
recovery_mode = st.radio("CHOOSE SCANNING PATTERN:", ["Name + 4 Digits", "8-Digit Numbers Only"], horizontal=True)

st.markdown("---")

# --- FILE UPLOADER & HINT ---
st.markdown('<div class="rgb-container">🛰️ Satellite Scanner Active</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

custom_hint = ""
if recovery_mode == "Name + 4 Digits":
    st.markdown('<div class="rgb-container">💡 Hint Engine Standby</div>', unsafe_allow_html=True)
    raw_hint = st.text_input("type_here", placeholder="Type name hint (e.g. Vikas)", label_visibility="collapsed")
    # Clean input: force uppercase and strip spaces
    custom_hint = "".join(raw_hint.split()).upper()

# --- COMMON NAMES DICTIONARY ---
COMMON_NAMES = [
    "AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU", 
    "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE", 
    "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA", 
    "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM", 
    "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI", 
    "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI", 
    "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE", 
    "KUMA", "SING", "MISH", "SHAR", "VERM", "GUPT", "YADA", "PATE", "CHAU", "KHAN",
    "RAWA", "NEGI", "BISH", "SAIN", "DHIL", "SIDD", "KAUR", "BALA", "ALOK", "ASIF",
    "BABU", "BALI", "BINK", "CHET", "DAKS", "ESHA", "FAIZ", "GOPL", "HARS", "ISHA"
]

# --- RECOVERY EXECUTION ---
if uploaded_file and st.button("🚀 EXECUTE RECOVERY ENGINE"):
    
    pdf_bytes = uploaded_file.read()
    found = False
    
    # TV TERMINAL MONITOR
    tv_screen = st.empty()
    progress_bar = st.progress(0)
    
    tv_screen.markdown("""
        <div class="tv-screen">
            > [SYSTEM_INIT] Booting Ultra Recovery Protocol v2026...<br>
            > [STATUS] Connecting to Satellite Scanner Matrix...
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)

    try:
        if recovery_mode == "Name + 4 Digits":
            search_list = []
            if custom_hint and len(custom_hint) >= 4:
                for i in range(len(custom_hint) - 3):
                    chunk = custom_hint[i:i+4]
                    search_list.extend([chunk, chunk.upper(), chunk.lower()])
            
            for name in COMMON_NAMES:
                if name not in search_list:
                    search_list.extend([name, name.lower()])
            
            search_list = list(dict.fromkeys(search_list))
            
            for idx, prefix in enumerate(search_list):
                # Live TV Screen Terminal Output
                tv_screen.markdown(f"""
                    <div class="tv-screen">
                        > [SYSTEM_ACTIVE] BRUTE-FORCE IN PROGRESS...<br>
                        > SCANNING PATTERN: <span style="color:#22d3ee;">{prefix}XXXX</span><br>
                        > TESTED PREFIXES: {idx+1}/{len(search_list)}
                    </div>
                """, unsafe_allow_html=True)
                
                progress_bar.progress((idx + 1) / len(search_list))
                
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            test_output = io.BytesIO()
                            pdf.save(test_output)
                            
                            st.balloons()
                            tv_screen.markdown(f"""
                                <div class="tv-screen" style="border-color: #10b981; box-shadow: 0 0 20px rgba(16,185,129,0.5);">
                                    > [SUCCESS] PDF PASSWORD DECRYPTED!<br>
                                    > UNLOCKED KEY: <span style="color:#f59e0b; font-size:20px;">{password}</span>
                                </div>
                            """, unsafe_allow_html=True)
                            
                            st.success(f"🔓 VERIFIED FOUND: {password}")
                            found = True
                            st.download_button("📥 DOWNLOAD UNLOCKED PDF", test_output.getvalue(), f"Unlocked_{password}.pdf")
                            break
                    except:
                        continue
                if found:
                    break

        else:  # 8-Digit Numbers Only Mode
            for n in range(100000000):
                password = f"{n:08d}"
                if n % 3000 == 0:
                    tv_screen.markdown(f"""
                        <div class="tv-screen">
                            > [SYSTEM_ACTIVE] NUMERIC SCAN IN PROGRESS...<br>
                            > CURRENT KEY TEST: <span style="color:#22d3ee;">{password}</span>
                        </div>
                    """, unsafe_allow_html=True)
                
                try:
                    with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                        test_output = io.BytesIO()
                        pdf.save(test_output)
                        
                        st.balloons()
                        tv_screen.markdown(f"""
                            <div class="tv-screen" style="border-color: #10b981; box-shadow: 0 0 20px rgba(16,185,129,0.5);">
                                > [SUCCESS] PDF PASSWORD DECRYPTED!<br>
                                > UNLOCKED KEY: <span style="color:#f59e0b; font-size:20px;">{password}</span>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        st.success(f"🔓 VERIFIED FOUND: {password}")
                        found = True
                        st.download_button("📥 DOWNLOAD UNLOCKED PDF", test_output.getvalue(), f"Unlocked_{password}.pdf")
                        break
                except:
                    continue
                if found:
                    break

        if not found:
            tv_screen.markdown("""
                <div class="tv-screen" style="border-color: #ef4444; color: #ef4444;">
                    > [FAILED] PASSWORD NOT FOUND IN CURRENT DICTIONARY.<br>
                    > PLEASE TRY ANOTHER HINT.
                </div>
            """, unsafe_allow_html=True)
            st.error("❌ Password not found or recovery failed.")

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("<br><center style='color:#64748b; font-size:12px; font-weight:600;'>VIKAS MISHRA PRIVATE SUITE © 2026</center>", unsafe_allow_html=True)
