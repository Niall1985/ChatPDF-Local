import fitz

def text_extractor(uploaded_files):
    pdf_text = {}
    for pdf_file in uploaded_files:
        doc = fitz.open(stream=pdf_file.read(), filetype = "pdf")
        text = "\n".join(page.get_text("text") for page in doc)
        pdf_text[pdf_file.name] = text
    return pdf_text