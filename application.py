import pandas as pd
from scripts.nlp_process import nlp_process
import streamlit as st

st.title('Doğal Dil İşleme')

uploaded_file = st.file_uploader("Upload a pdf file into the model.", type=['pdf'], accept_multiple_files=False,
                                 key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False,
                                 label_visibility="visible")

doc = None

if st.button("Submit"):
    if uploaded_file is not None:
        doc = nlp_process(uploaded_file.getbuffer().tobytes())
    else:
        st.write("Please upload a file.")

if doc is not None:
    data_set = pd.DataFrame(
        {
            "Text": [ent.text for ent in doc.ents],
            "Label": [ent.label_ for ent in doc.ents]
        }
    )
    st.write(data_set)
    st.download_button('Download CSV', data=data_set.to_csv(), file_name=uploaded_file.name,
                       mime='text/csv')
