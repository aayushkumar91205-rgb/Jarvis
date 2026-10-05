import streamlit as st
from fpdf import FPDF
import tempfile
import os

def render_image_module():
    st.subheader("📄 Action Hub & Study PDF Generator")
    st.markdown("Generate clean, printable A4 reference sheets and study guides.")
    
    with st.form("pdf_gen_form"):
        topic_title = st.text_input("Document Title", value="Class 10 Mathematics - Circle Theorems Reference")
        topic_content = st.text_area("Document Content / Formulas", value="1. Tangent perpendicular to radius.\n2. Tangents from external point are equal in length.")
        
        if st.form_submit_button("📥 Generate Printable PDF"):
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 16)
                pdf.cell(200, 10, txt=topic_title, ln=True, align='C')
                pdf.ln(10)
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, txt=topic_content)
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    pdf.output(tmp.name)
                    tmp_path = tmp.name
                
                with open(tmp_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download PDF for A4 Printing",
                        data=f,
                        file_name="Jarvis_Study_Reference.pdf",
                        mime="application/pdf"
                    )
                st.success("PDF generated successfully!")
            except Exception as e:
                st.error(f"PDF generation error: {e}")
