import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

# Example usage
pdf_path = 'C:\\Users\\hajny\\Dropbox\\a1\\maj.pdf' 
text = extract_text_from_pdf(pdf_path)
print(text[:500])  # Print the first 500 characters to verify
