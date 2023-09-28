<!-- ABOUT THE PROJECT -->
## About The Project


This project is for converging .pdf files into images and then extracting the text on the images with OCR technologies. After that the program gives the text into a NER algorithm using spacy. The entities are then extracted into a .csv file.

This project is designed for the English Language.


<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mmentese21/nlp.git
   ```

2. Install the required libraries.
   ```sh
   pip install -r requirements.txt
   ```
3. Install the English language suite.
    ```sh
   python3 -m spacy download en
   ```
   
4. Install the tesseract-ocr. 
    ```sh
   apt-get -y install tesseract-ocr
   ```

5. Install the pdf2image package here: https://pdf2image.readthedocs.io/en/latest/installation.html

### Docker Image

https://hub.docker.com/r/mmentese21/ocrnlp

    ```sh
   docker run -p 8501:8501 [iD]
   ```

