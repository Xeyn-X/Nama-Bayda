import numpy as np
import tensorflow as tf
from tensorflow import keras
import streamlit as st
import pandas as pd
import pickle
import random
import re
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def gender_detect(name):
    inputs = [name]

    inputs = [re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))', r' \1', i) for i in inputs]

    # Load the tokenizer
    with open('./tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
                           
    testing_sequences = tokenizer.texts_to_sequences(inputs)
    testing_padded = pad_sequences(testing_sequences,maxlen=9, truncating='post',padding='post')
    gender = tf.keras.models.load_model('./name_gender.keras')
    
    ans = gender.predict(testing_padded)
    
    # Apply threshold
    binary_result = (ans >= 0.5).astype(int)

    if binary_result == 0:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender

def generate_names():
    max_sequence_length = 10

    # Get unique elements and create dictionaries
    chars = sorted(list(set(concat_names)))  # Flatten and get unique elements
    num_chars = len(chars)
    
    char2idx = {c: i for i, c in enumerate(chars)}
    idx2char = {i: c for i, c in enumerate(chars)}

    
    r = np.random.choice(len(concat_names)-1)
    r2 = r-max_sequence_length

    sequence = concat_names[r2:r-1] + '\n'

    new_names = []

    while len(new_names) < 1:
        x = np.zeros((1, max_sequence_length, num_chars))

        for i, char in enumerate(sequence):
            x[0, i, char2idx[char]] = 1

        probs = model.predict(x, verbose=0)[0]
        probs /= probs.sum()

        next_idx = np.random.choice(len(probs), p=probs)

        next_char = idx2char[next_idx]

        sequence = sequence[1:] + next_char

        if next_char == '\n':
            gen_name = [name for name in sequence.split('\n')][1]

            if len(gen_name) > 4 and gen_name[0] == gen_name[1]:
                gen_name = gen_name[1:]

            if len(gen_name) > 4 and len(gen_name) <= 8:

                if gen_name not in sequences_no_zeros + new_names:
                    new_names.append(gen_name)


                    # Split the sequence and convert to integers
                    new_names = [int(num) for num in new_names[0].split()]


                    # Convert sequence to words
                    words = [key for num in new_names for key, value in word_index.items() if value == num]

                    # Join words into a single string
                    result = "".join(words)

                    if gender_detect(result) == gen:
                        
                        return check_name_meaning(result, meaning_data)
                    else:
                        return generate_names()
                        

# Function to check the meaning of each part of the name
def check_name_meaning(name, data):
    name_syllable = re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))', r' \1', name)
    
    # Split the Burmese name by each word
    name_parts = name_syllable.split()
    meanings = []  # List to store meanings
    
    # Loop through each part of the name
    for part in name_parts:
        if part in data:  # Check if part has a meaning in the dictionary
            if data[part] not in meanings:  # Add meaning if not a duplicate
                meanings.append(data[part])
       
    # Format the result as a comma-separated string
    result = f"{name}  <span style='color:orange;'>({', '.join(meanings)})</span>" if meanings else "(None)"
    return result
        
# Load data from JSON file
with open('./Burmese_Name_Meaning.json', 'r', encoding='utf-8') as file:
    meaning_data = json.load(file)


with open("./concat_names.pkl", "rb") as file:
    concat_names = pickle.load(file)

with open("./word_index.pkl", "rb") as file:
    word_index = pickle.load(file)

with open("./sequences_no_zeros.pkl", "rb") as file:
    sequences_no_zeros = pickle.load(file)
    
# Assuming you have saved the model at 'path_to_model'
model_path = './BurmeseNameGen.keras'

# Load the model without custom CTC loss
model = tf.keras.models.load_model(model_path)


form = st.form("my_form")
form.title("Burmese Name Generator")
number = form.number_input("Generated Name Count", step=1)
gen = form.selectbox(
        "Select Gender",
        ["Male", 
    "Female"
    ])

button = form.form_submit_button("Generate", type="primary")
form.markdown(":gray[<p style='font-size:12px;'>Copyright © 2024 Hein Htet Arkar Mg</p>]", unsafe_allow_html=True)
if button:
    for _ in range(number):
        st.markdown(f"""<div style='text-align: center;'><span style='font-size:16px;'> {generate_names()}</span></div>""", unsafe_allow_html=True)
    
