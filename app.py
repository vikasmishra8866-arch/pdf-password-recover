import streamlit as st
import pikepdf
import io
import time
import re

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vikas Mishra | Ultra Recovery Pro",
    page_icon="🔑",
    layout="centered"
)

# --- CUSTOM ULTRA PRO DEEP OCEAN CSS ---
st.markdown("""
    <style>
    /* DEEP OCEAN HYDRO BACKGROUND WITH PULSE */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d284f 0%, #031329 85%) !important;
        color: #f8fafc !important;
        font-family: 'Inter', sans-serif;
    }

    /* CARD CONTAINER */
    .hydro-card {
        background: #0b1d3a;
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }

    /* HEADER TEXT */
    .header-title {
        color: #f59e0b;
        font-weight: 900;
        letter-spacing: 2px;
        text-align: center;
        margin-bottom: 0px;
    }

    .sub-header {
        color: #94a3b8;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 5px;
    }

    /* HACKER TV TERMINAL SCREEN */
    .tv-terminal {
        background: #020b14;
        border: 2px solid #06b6d4;
        border-radius: 14px;
        padding: 16px;
        font-family: 'Courier New', monospace;
        color: #00ff66;
        box-shadow: inset 0 0 15px rgba(6, 182, 212, 0.25);
        min-height: 120px;
        margin-top: 15px;
        margin-bottom: 15px;
        line-height: 1.5;
        font-size: 0.9rem;
    }

    /* INPUT STYLING */
    .stTextInput input {
        border: 1px solid rgba(6, 182, 212, 0.4) !important;
        background: rgba(3, 19, 41, 0.8) !important;
        color: #ef4444 !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-radius: 12px !important;
    }

    /* BUTTON GLOW */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #06b6d4 0%, #0284c7 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        border-radius: 12px !important;
        height: 52px !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
        width: 100%;
    }

    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 25px rgba(6, 182, 212, 0.7);
    }

    /* DOWNLOAD BUTTON */
    div.stDownloadButton > button {
        background: #10b981 !important;
        color: white !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
        border-radius: 12px !important;
        height: 52px !important;
        width: 100%;
        border: none !important;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# --- DEFAULT DICTIONARY FOR FAST BRUTEFORCE ---
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

# --- UI CONTENT ---
st.markdown("""
    <div class="hydro-card">
        <h1 class="header-title">ULTRA RECOVERY PRO</h1>
        <p class="sub-header">💎 Managed by: <b style="color: #f59e0b;">VIKAS MISHRA</b></p>
    </div>
""", unsafe_allow_html=True)

# MODE SELECTION
st.markdown("<div style='color: #06b6d4; font-size: 0.8rem; font-weight: bold; margin-bottom: 5px;'>⚙️ RECOVERY MODE SELECTION</div>", unsafe_allow_html=True)
recovery_mode = st.radio(
    "",
    ["Name + 4 Digits", "8-Digit Numbers Only"],
    horizontal=True,
    label_visibility="collapsed"
)

# FILE UPLOADER
uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])

# HINT INPUT
custom_hint = ""
if recovery_mode == "Name + 4 Digits":
    custom_hint = st.text_input("NAME HINT", placeholder="TYPE NAME HINT (E.G. VIKAS)").strip().upper()
    custom_hint = re.sub(r'[^A-Z0-9]', '', custom_hint)

# RECOVERY PROCESS
if uploaded_file and st.button("🚀 EXECUTE RECOVERY ENGINE"):
    pdf_bytes = uploaded_file.read()
    found_password = None
    unlocked_pdf_stream = io.BytesIO()

    # TV SCREEN DISPLAY PLACEHOLDER
    tv_screen = st.empty()
    progress_bar = st.progress(0)

    tv_screen.markdown("<div class='tv-terminal'>> [SYSTEM_INIT] Booting Ultra Recovery Engine (pikepdf C++ Backend)...<br>> [STATUS] Connecting Decryption Matrix...</div>", unsafe_allow_html=True)

    start_time = time.time()

    if recovery_mode == "Name + 4 Digits":
        search_prefixes = []
        if len(custom_hint) >= 4:
            for i in range(len(custom_hint) - 3):
                search_prefixes.append(custom_hint[i:i+4])
        
        # Merge dictionary
        search_prefixes.extend(COMMON_NAMES)
        # Unique preserving order
        search_prefixes = list(dict.fromkeys(search_prefixes))

        total_prefixes = len(search_prefixes)

        for idx, prefix in enumerate(search_prefixes):
            tv_screen.markdown(f"<div class='tv-terminal'>> [SCANNING] PATTERN: [ <b style='color:#f59e0b;'>{prefix}XXXX</b> ]<br>> Testing digits 0000 to 9999...</div>", unsafe_allow_html=True)
            progress_bar.progress((idx + 1) / total_prefixes)

            for n in range(10000):
                test_pass = f"{prefix}{n:04d}"
                try:
                    # High-speed pikepdf C++ decryption engine
                    with pikepdf.open(io.BytesIO(pdf_bytes), password=test_pass) as pdf:
                        pdf.save(unlocked_pdf_stream)
                        found_password = test_pass
                        break
                except pikepdf.PasswordError:
                    continue
                except Exception:
                    continue

            if found_password:
                break

    else:  # 8-Digit Numbers Only
        tv_screen.markdown("<div class='tv-terminal'>> [SCANNING] 8-DIGIT NUMERIC BRUTE-FORCE STARTED...</div>", unsafe_allow_html=True)
        for n in range(100000000):
            test_pass = f"{n:08d}"
            if n % 10000 == 0:
                tv_screen.markdown(f"<div class='tv-terminal'>> [SCANNING] Testing Range: <b style='color:#f59e0b;'>{test_pass}</b>...</div>", unsafe_allow_html=True)
                progress_bar.progress(min(n / 100000000, 1.0))

            try:
                with pikepdf.open(io.BytesIO(pdf_bytes), password=test_pass) as pdf:
                    pdf.save(unlocked_pdf_stream)
                    found_password = test_pass
                    break
            except pikepdf.PasswordError:
                continue
            except Exception:
                continue

    elapsed_time = round(time.time() - start_time, 2)

    # RESULT SCREEN
    if found_password:
        tv_screen.markdown(f"""
            <div class='tv-terminal' style='border-color: #10b981;'>
                > <b style='color: #10b981;'>[SUCCESS] PDF UNLOCKED SUCCESSFULLY!</b><br>
                > Found Password: <b style='color: #f59e0b;'>{found_password}</b><br>
                > Time Taken: {elapsed_time} Seconds
            </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        
        st.markdown(f"<h3 style='text-align: center; color: #10b981;'>🔓 VERIFIED FOUND: <span style='color: #f59e0b;'>{found_password}</span></h3>", unsafe_allow_html=True)
        
        st.download_button(
            label="📥 DOWNLOAD UNLOCKED PDF",
            data=unlocked_pdf_stream.getvalue(),
            file_name=f"Unlocked_{found_password}.pdf",
            mime="application/pdf"
        )
    else:
        tv_screen.markdown("""
            <div class='tv-terminal' style='border-color: #ef4444;'>
                > <b style='color: #ef4444;'>[FAILED] PASSWORD NOT FOUND</b><br>
                > Please verify the hint or try a different pattern.
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><div style='text-align: center; font-size: 0.75rem; color: #64748b;'>VIKAS MISHRA PRIVATE SUITE © 2026</div>", unsafe_allow_html=True)
