import gradio as gr
from PyPDF2 import PdfReader
import pytesseract


class OCR:
    def __init__(self):
        self.path = r"D:/Tesseract-OCR/tesseract.exe"  # path to your tesseract exe file

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


# Function to process the file and extract text
def ocr_function(file):
    ocr = OCR()
    
    if file.name.lower().endswith((".png", ".jpg", ".jpeg")):
        # Extract text from image
        extracted_text = ocr.extract(file.name)
        return f"Extracted Text from Image: {extracted_text}"

    elif file.name.lower().endswith(".pdf"):
        # Extract text from PDF
        extracted_text = ocr.extract_from_pdf(file.name)
        return f"Extracted Text from PDF: {extracted_text}"

    else:
        return "Unsupported file format. Please upload a valid image or PDF."


# Gradio Interface
iface = gr.Interface(
    fn=ocr_function, 
    inputs=gr.File(label="Upload Image or PDF"), 
    outputs=gr.Textbox(label="Extracted Text"), 
    live=True
)

if __name__ == "__main__":
    iface.launch()
