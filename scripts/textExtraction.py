import pytesseract


def extract(image):
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    generated_text = pytesseract.image_to_string(image, lang="tur")

    return generated_text
