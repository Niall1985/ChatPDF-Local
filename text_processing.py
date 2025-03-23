import fitz
import re


def files_for_processing(uploaded_files):
    pdf_text = ""
    for file in uploaded_files:
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            
            for page in doc:
                pdf_text += page.get_text() + "\n"

    cleaned_text = clean_text(pdf_text)
    return cleaned_text
    

def clean_text(text):
    text = re.sub(f'\s+', '',text).strip()
    text = text.encode('ascii', 'ignore').decode()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text