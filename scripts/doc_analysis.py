import pathlib

import spacy
import csv


def analiz(text):
    nlp = spacy.load("tr_core_news_trf")
    doc = nlp(text)
    return doc