from scripts.doc_analysis import analiz
from scripts.textExtraction import extract
from scripts.typeConversion import convert_pdf


def nlp_process(documents):
    # convert the pdf file into images and add them into images dir

    imag = convert_pdf(documents)

    generated_text = ''
    for elem in imag:
        generated_text += extract(elem)

    return analiz(generated_text)
