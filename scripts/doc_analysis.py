import spacy


def analiz(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return doc
