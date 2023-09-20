from pdf2image import convert_from_bytes


def convert_pdf(image_bytes):
    images = convert_from_bytes(image_bytes, poppler_path=r"poppler-23.08.0\Library\bin",fmt='jpeg')
    return images
