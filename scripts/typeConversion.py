from pdf2image import convert_from_bytes


def convert_pdf(image_bytes):
    images = convert_from_bytes(image_bytes, fmt='jpeg')
    return images
