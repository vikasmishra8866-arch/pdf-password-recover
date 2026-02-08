import streamlit as st
import pikepdf
import io

st.set_page_config(page_title="Pawan PDF Unlocker", page_icon="🔓")

st.title("🔓 Smart PDF Password Recovery")
st.write("Pattern: Name ke 4 Letters + 4 Random Digits")

uploaded_file = st.file_uploader("Locked PDF Upload Karein", type=["pdf"])
full_name = st.text_input("Customer ka Pura Naam dalein (e.g. GAURAV)", "").upper().replace(" ", "")

if uploaded_file and full_name:
    if len(full_name) < 4:
        st.error("Naam kam se kam 4 aksharon ka hona chahiye!")
    else:
        if st.button("Crack Password Now 🚀"):
            pdf_bytes = uploaded_file.read()
            found = False
            
            # Step 1: Naam se saare 4-letter combinations nikalna
            # Example: GAURAV -> GAUR, AURA, URAV
            possible_prefixes = []
            for i in range(len(full_name) - 3):
                possible_prefixes.append(full_name[i:i+4])
            
            # Step 2: Progress Bar setup
            status_text = st.empty()
            bar = st.progress(0)
            
            total_prefixes = len(possible_prefixes)
            
            try:
                for idx, prefix in enumerate(possible_prefixes):
                    status_text.text(f"Scanning combinations for: {prefix}...")
                    bar.progress((idx + 1) / total_prefixes)
                    
                    # Step 3: 0000 se 9999 tak check karna
                    for n in range(10000):
                        password = f"{prefix}{n:04d}"
                        
                        try:
                            with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                                st.success(f"🎊 FOUND IT! Password: **{password}**")
                                
                                # Unlocked file download option
                                out_buf = io.BytesIO()
                                pdf.save(out_buf)
                                st.download_button("📥 Download Unlocked PDF", out_buf.getvalue(), "unlocked_file.pdf")
                                
                                found = True
                                break
                        except pikepdf.PasswordError:
                            continue
                    
                    if found: break
                
                if not found:
                    st.error("❌ Password nahi mila. Kya naam ki spelling sahi hai?")
                    
            except Exception as e:
                st.error(f"Technical Error: {e}")

st.markdown("---")
st.caption("Tip: Agar naam se kaam na chale, toh 'PAWAN' ya 'AUTO' try karein.")
