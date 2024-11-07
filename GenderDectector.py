import numpy as np
import tensorflow as tf
from tensorflow import keras
import streamlit as st
import pandas as pd
import pickle
import random
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def gender_detect(name):
    inputs = [name]

    inputs = [re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))', r' \1', i) for i in inputs]

    # Load the tokenizer
    with open('/Users/heinhtetarkarmg/Downloads/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
                           
    testing_sequences = tokenizer.texts_to_sequences(inputs)
    testing_padded = pad_sequences(testing_sequences,maxlen=9, truncating='post',padding='post')
    gender = tf.keras.models.load_model('/Users/heinhtetarkarmg/Downloads/name_gender.keras')
    
    ans = gender.predict(testing_padded)
    
    # Apply threshold
    binary_result = (ans >= 0.5).astype(int)

    if binary_result == 0:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender


form = st.form("my_form")
form.markdown("<spam style='font-size:30px; font-weight:bold;'>Gender Detection</spam><spam style='font-size:15px; font-weight:bold; color: gray;'> for Burmese Name</spam>", unsafe_allow_html=True)
name = form.text_input("Enter Burmese Name")
button = form.form_submit_button("Detection", type="primary")
form.markdown(":gray[<p style='font-size:12px;'>Copyright © 2024 Hein Htet Arkar Mg</p>]", unsafe_allow_html=True)
if button:
    st.write(gender_detect(name))