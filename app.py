import streamlit as st
import pikepdf
from itertools import product
import io

st.set_page_config(page_title="PDF Password Recovery", page_icon="🔓")

st.title("🔓 PDF Password Recover Tool")
st.info("Ye tool aapke pattern (4 Letters + 4 Digits) par kaam karega.")

# Inputs
uploaded_file = st.file_uploader("Apni Locked PDF Upload Karein", type=["pdf"])
name_part = st.text_input("Naam ke pehle 4 Capital Letters dalein (Example: SHYA)", "").upper()

if uploaded_file and name_part:
    if len(name_part) != 4:
        st.warning("Kripya sirf 4 letters dalein.")
    else:
        if st.button("Password Recover Shuru Karein"):
            found = False
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # 0001 se 9999 tak ke saare combinations
            total_attempts = 10000 
            
            try:
                # PDF ko read karne ki koshish
                pdf_bytes = uploaded_file.read()
                
                for i in range(1, 10000):
                    # 4 digit number banana (Example: 1 -> 0001)
                    num_part = f"{i:04d}"
                    password = name_part + num_part
                    
                    # UI Update (har 500 attempts par)
                    if i % 500 == 0:
                        progress_bar.progress(i / total_attempts)
                        status_text.text(f"Checking: {password}...")

                    try:
                        # Password check karna
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.success(f"✅ Password Mil Gaya! Aapka Password hai: **{password}**")
                            
                            # Unlock karke download dene ka option
                            output = io.BytesIO()
                            pdf.save(output)
                            st.download_button("📥 Unlocked PDF Download Karein", output.getvalue(), file_name="unlocked.pdf")
                            
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                
                if not found:
                    st.error("❌ Diye gaye pattern mein password nahi mila. Kripya letters check karein.")
                
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Note: Ye sirf aapke bhule hue passwords ke liye hai.")
