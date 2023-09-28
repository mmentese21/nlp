FROM python:3.9

WORKDIR /app
RUN apt-get update
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install poppler-utils
RUN pip3 install spacy==3.4.4 pytesseract==0.3.10 requests==2.31.0 transformers==4.25.1 Pillow==9.3.0 pdf2image==1.16.3 stcli==0.2.1 streamlit==1.26.0 numpy==1.25.2 pandas==2.1.0
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
COPY ./scripts /app/scripts
COPY ./application.py /app/application.py

RUN python3 -m spacy download en
ENTRYPOINT ["streamlit", "run", "application.py", "--server.port=8501", "--server.address=0.0.0.0"]
