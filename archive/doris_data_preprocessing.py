import os
import pdfplumber

current_directory = os.path.dirname(os.path.realpath(__file__))
pdf_folder = os.path.join(current_directory, '..', 'data', 'Downloaded_Documents')

#pdf_folder = '/Users/nathanstorey/Documents/Visual Studio Code/Civic Roam Chat/civicroamchat/data'
#pdf_folder = 'data'  # or the absolute path to the folder containing the PDF files

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

print("Content of the current folder:", os.listdir())

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

pdf_contents = []
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    pdf_content = read_pdf(pdf_path)
    pdf_contents.append(pdf_content)

print("Loaded PDF files:")
for pdf_file in pdf_files:
    print(f" - {pdf_file}")

print(f"\nTotal number of PDF files loaded: {len(pdf_files)}")

import os
import shutil
from PyPDF2 import PdfReader

def is_ocr_required(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            if len(text.strip()) > 0:
                return False  # OCR is not required
    return True  # OCR is required

current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.join(current_directory, '..', 'data', 'Downloaded_Documents')
ocr_required_folder = os.path.join(current_directory, '..', 'data', 'OCR_Required')
ocr_not_required_folder = os.path.join(current_directory, '..', 'data', 'OCR_Not_Required')

os.makedirs(ocr_required_folder, exist_ok=True)
os.makedirs(ocr_not_required_folder, exist_ok=True)

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    if is_ocr_required(pdf_path):
        print(f"OCR is required for {pdf_file}")
        shutil.move(pdf_path, os.path.join(ocr_required_folder, pdf_file))
    else:
        print(f"OCR is not required for {pdf_file}")
        shutil.move(pdf_path, os.path.join(ocr_not_required_folder, pdf_file))