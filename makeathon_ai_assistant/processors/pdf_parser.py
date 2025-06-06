import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    if not text.strip():
        from processors.aws_textract import extract_text_textract
        text = extract_text_textract(pdf_path)
    return text
