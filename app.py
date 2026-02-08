import streamlit as st
import pikepdf
import io

st.set_page_config(page_title="Pawan PDF Unlocker Pro", page_icon="🔓")

st.title("🔓 Advanced PDF Password Recovery")
st.write("Pattern: 4 Letters (Name) + 4 Digits (Number)")

# --- BIG INDIAN NAMES LIST (Expanded) ---
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

uploaded_file = st.file_uploader("Locked PDF Upload Karein", type=["pdf"])

# --- NEW OPTION: CUSTOM HINT BOX ---
custom_hint = st.text_input("Kuch yaad hai? (e.g. Naam ke 4 Letters)", "").upper().strip()

if uploaded_file:
    if st.button("Start Deep Recovery 🚀"):
        pdf_bytes = uploaded_file.read()
        found = False
        status_text = st.empty()
        bar = st.progress(0)
        
        # Check list taiyar karna (Pehle user ki hint, phir baki list)
        search_list = []
        if custom_hint and len(custom_hint) == 4:
            search_list.append(custom_hint)
        
        # Baki names ko list mein add karna (duplicate hatakar)
        for name in COMMON_NAMES:
            if name not in search_list:
                search_list.append(name)
        
        total_names = len(search_list)
        
        try:
            for idx, prefix in enumerate(search_list):
                status_text.text(f"Testing Pattern: {prefix}XXXX ({idx+1}/{total_names})")
                bar.progress((idx + 1) / total_names)
                
                # 0000 se 9999 tak check karna
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.success(f"🎊 FOUND IT! Password: **{password}**")
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 Download Unlocked PDF", out_buf.getvalue(), "unlocked.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break
            
            if not found:
                st.error("❌ Password nahi mila. Kripya koi nayi hint try karein.")
                    
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.info("Tip: Agar aapne koi hint dali hai, toh ye sabse pehle use hi check karega.")
