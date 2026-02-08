import streamlit as st
import pikepdf
import io

st.set_page_config(page_title="Indian PDF Unlocker", page_icon="🔓")

st.title("🔓 Smart PDF Password Recovery")
st.write("Pattern: Common Indian Names (4 Letters) + 4 Random Digits")

# --- TOP COMMON INDIAN NAMES LIST ---
# Inke shuru ke 4 letters system check karega
COMMON_NAMES = [
    "AMIT", "ANIL", "ARUN", "AJAY", "ABHI", "AKAS", "AMAN", "ANSH", "ANUP", "ASHU",
    "DEEP", "DEVA", "DINE", "GAUR", "GURU", "HARI", "HEMA", "INDU", "JAYA", "JAYE",
    "JYOT", "KAMA", "KAPI", "KIRA", "KUNA", "LALU", "MADH", "MANO", "MEEN", "MOHA",
    "MUKA", "NEER", "NITI", "PANK", "PAWA", "PIYU", "POOJ", "PRAD", "PRAK", "PRAM",
    "RAHU", "RAJA", "RAJE", "RAKE", "RAMA", "RANI", "RAVI", "RISH", "ROHA", "ROHI",
    "SACH", "SAME", "SANJ", "SANT", "SARA", "SATI", "SHIV", "SHYA", "SONU", "SUMI",
    "SUNI", "SURA", "TARA", "UMES", "VIKA", "VIMA", "VINA", "VINO", "VIVE", "YOGE"
]

uploaded_file = st.file_uploader("Locked PDF Upload Karein", type=["pdf"])

if uploaded_file:
    if st.button("Start Deep Indian Scan 🚀"):
        pdf_bytes = uploaded_file.read()
        found = False
        
        status_text = st.empty()
        bar = st.progress(0)
        
        total_names = len(COMMON_NAMES)
        
        try:
            for idx, prefix in enumerate(COMMON_NAMES):
                status_text.text(f"Scanning for Name Pattern: {prefix}...")
                bar.progress((idx + 1) / total_names)
                
                # Har naam ke liye 0000 se 9999 tak check karna
                for n in range(10000):
                    password = f"{prefix}{n:04d}"
                    
                    try:
                        # Streamlit ki speed badhane ke liye hum memory se read karenge
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.success(f"🎊 FOUND IT! Password: **{password}**")
                            
                            out_buf = io.BytesIO()
                            pdf.save(out_buf)
                            st.download_button("📥 Download Unlocked PDF", out_buf.getvalue(), "unlocked_file.pdf")
                            
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                
                if found: break
            
            if not found:
                st.error("❌ Password nahi mila. Kripya koi specific name hint dalein.")
                    
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.info("Tip: Ye tool India ke 70+ popular name patterns check karta hai.")
