import streamlit as st
import pikepdf
import io
from itertools import product
import string

st.set_page_config(page_title="PDF Ultra Recovery", page_icon="🔑")

st.title("🔓 PDF Universal Password Recover")
st.write("Ye tool A-Z ke letters aur numbers ke combinations check karega.")

uploaded_file = st.file_uploader("Locked PDF Upload Karein", type=["pdf"])

# Options for Randomness
col1, col2 = st.columns(2)
with col1:
    char_limit = st.number_input("Letters Kitne hain? (e.g. 4)", min_value=1, max_value=6, value=4)
with col2:
    num_limit = st.number_input("Digits Kitne hain? (e.g. 4)", min_value=1, max_value=6, value=4)

# Yahan aap specific letters de sakte hain jo aapko yaad hain
search_letters = st.text_input("Kaunse letters use karein? (Default: A-Z)", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if uploaded_file:
    if st.button("Deep Scan Shuru Karein 🚀"):
        pdf_bytes = uploaded_file.read()
        found = False
        
        status = st.empty()
        progress = st.progress(0)
        
        # Numbers 0000 to 9999 ki list
        numbers = [f"{i:0{num_limit}d}" for i in range(10**num_limit)]
        
        # Agar user ne specific 4 letters diye hain (Jaise 'SHYA'), to sirf unke combinations:
        # Lekin agar A-Z check karna hai to ye bahut heavy ho jayega.
        
        # Filhal hum aapke bataye pattern (NAME PART + NUMBER PART) par brute force kar rahe hain
        # Yahan hum example ke liye letters ka combination generate kar rahe hain
        
        st.warning("Scanning start ho gayi hai... Ismein time lag sakta hai.")

        try:
            # Note: Pure A-Z (4 letters) = 4,56,976 combinations. 
            # Saath mein 4 digits = 4.5 Billion combinations (Ye server par crash ho jayega).
            # Isliye hum "Name Hint" ka use kar rahe hain.
            
            # Agar aapko letters yaad nahi hain, toh ye pattern kaam karega:
            possible_names = ["".join(x) for x in product(search_letters, repeat=char_limit)]
            
            total = len(possible_names)
            
            for idx, name in enumerate(possible_names):
                status.text(f"Testing Names starting with: {name}...")
                progress.progress((idx + 1) / total)
                
                for num in numbers:
                    password = name + num
                    try:
                        with pikepdf.open(io.BytesIO(pdf_bytes), password=password) as pdf:
                            st.success(f"🎊 SUCCESS! Password mil gaya: **{password}**")
                            output = io.BytesIO()
                            pdf.save(output)
                            st.download_button("📥 Unlock PDF Download", output.getvalue(), "unlocked.pdf")
                            found = True
                            break
                    except pikepdf.PasswordError:
                        continue
                if found: break

            if not found:
                st.error("Password nahi mila. Try different letters.")

        except Exception as e:
            st.error(f"Error occurred: {e}")
