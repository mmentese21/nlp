FROM python:3.9
ADD application.py /
RUN apt-get update
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install poppler-utils
RUN pip3 install spacy==3.4.4 pytesseract==0.3.10 requests==2.31.0 transformers==4.25.1 Pillow==9.3.0 pdf2image==1.16.3 stcli==0.2.1 streamlit==1.26.0 numpy==1.25.2 pandas==2.1.0
RUN pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_trf/resolve/main/tr_core_news_trf-any-py3-none-any.whl

COPY . .
CMD ["streammlit", "run", "./application.py"]

