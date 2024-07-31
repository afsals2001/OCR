import pytesseract
from PyPDF2 import PdfReader

import os


class OCR:
    def __init__(self):
        self.path = r""      #path to your tesseract exe file

    def extract(self, filename):
        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            print(e)
            return "Error"

    def extract_from_pdf(self, filename):
        try:
            text = ""
            with open(filename, 'rb') as file:
                reader = PdfReader(file)

                for page in reader.pages:

                    text += page.extract_text()
            return text
        except Exception as e:
            print(e)
            return "Error"


ocr = OCR()
text = ocr.extract("text.png")
print(text)

text_from_pdf = ocr.extract_from_pdf("Replit for Business.pdf")
print("\nText from PDF: ")
print(text_from_pdf)
