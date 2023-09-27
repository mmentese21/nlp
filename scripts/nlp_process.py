from scripts.doc_analysis import analiz
from scripts.textExtraction import extract
from scripts.typeConversion import convert_pdf


def nlp_process(documents):
    imag = convert_pdf(documents)
    generated_text = ''
    for elem in imag:
        generated_text += extract(elem)
    return analiz(generated_text)
