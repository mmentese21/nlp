import pytesseract


def extract(image):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    generated_text = pytesseract.image_to_string(image, lang="eng")

    return generated_text
