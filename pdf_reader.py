import pdfplumber
from utils import clean_text

def extract_text_from_pdf(file_path: str) -> str:
    """قراءة نص من PDF بالكامل وتنظيفه."""
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return clean_text(text)
