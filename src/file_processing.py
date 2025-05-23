import PyPDF2
import pandas as pd

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_txt(txt_file):
    """Extract text from TXT file."""
    return txt_file.read().decode("utf-8")

def extract_data_from_csv(csv_file):
    """Extract data from CSV file."""
    return csv_file.read().decode("utf-8")

def extract_data_from_excel(excel_file):
    """Extract data from Excel file as CSV-like text."""
    df = pd.read_excel(excel_file)
    return df.to_csv(index=False)

def process_files(uploaded_files):
    """Process uploaded files and extract text content."""
    documents = []
    for file in uploaded_files:
        if file.type == "application/pdf":
            documents.append(extract_text_from_pdf(file))
        elif file.type == "text/plain":
            documents.append(extract_text_from_txt(file))
        elif file.type == "text/csv":
            documents.append(extract_data_from_csv(file))
        elif file.type in [
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/vnd.ms-excel"
        ]:
            documents.append(extract_data_from_excel(file))
        else:
            print(f"Unsupported file type: {file.type}")
    return documents
