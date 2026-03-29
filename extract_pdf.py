import sys
import subprocess
import os
try:
    import PyPDF2
except ImportError:
    print("Installing PyPDF2...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2", "--quiet"])
    import PyPDF2

def extract():
    try:
        reader = PyPDF2.PdfReader('D:/Resume/Resume_Sameer-Saha.pdf')
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        with open('D:/Resume/Site/extracted_resume.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Successfully extracted text to D:/Resume/Site/extracted_resume.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract()
