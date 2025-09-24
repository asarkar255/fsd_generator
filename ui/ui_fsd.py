import streamlit as st
from fsd_generator import generate_fsd
from formatter import fsd_to_docx

st.title("SAP ABAP → FSD Generator")

code = st.text_area("Paste ABAP Code")
if st.button("Generate FSD"):
    with st.spinner("Analyzing ABAP code..."):
        fsd = generate_fsd(code)
        st.json(fsd)
        if "error" not in fsd:
            filename = fsd_to_docx(fsd, "Generated_FSD.docx")
            with open(filename, "rb") as f:
                st.download_button("Download FSD (Word)", f, file_name="FSD.docx")
