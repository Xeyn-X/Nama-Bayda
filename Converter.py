import streamlit as st
import csv
import re
from itertools import product

# Load data from CSV file
data = {}
covverter_csv = './Converter.csv'
with open(covverter_csv, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if there is one
    for row in reader:
        if len(row) >= 2:  # Ensure there are at least two columns (Name, Meaning)
            data[row[0]] = row[1]

# Load data from CSV file
special_name = {}
with open('./SpecialName.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if there is one
    for row in reader:
        if len(row) >= 2:  # Ensure there are at least two columns (Name, Meaning)
            special_name[row[0]] = row[1]

def check_special_name(name):

    # Split syllable_name into individual words
    syllables = name.split()

    # Initialize a result list to store the replaced syllables
    result = []

    # Iterate through pairs of syllables
    i = 0
    while i < len(syllables):
        # Combine current and next syllable for matching
        if i < len(syllables) - 1:
            combined_syllable = syllables[i] + " " + syllables[i + 1]
            # Check if combined syllable is in data
            if combined_syllable in special_name:
                result.append(special_name[combined_syllable])  # Add the replacement
                i += 2  # Skip the next syllable since it's already matched
                continue

        # If no match, add the current syllable as is
        result.append(syllables[i])
        i += 1

    # Join the result back into a single string
    output = " ".join(result)

    return output

# Function to check the meaning of each part of the name
def check_name_meaning(name, data):

    name_syllable = re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))', r' \1', name)


    name_syllable = check_special_name(name_syllable)


    # Split the Burmese name by each word
    name_parts = name_syllable.split()
    meanings = []  # List to store meanings

    # Check for meanings in the CSV data
    for part in name_parts:
        if part in data:
            meanings.append(data[part])# Check if part has a meaning in the dictionary
            

    # Format the result as a comma-separated string
    result = f"{' '.join(meanings)}" if meanings else "(None)"
    return result

# Step 1: Load the existing CSV file and swap columns
def swap_csv_columns(input_csv, output_csv):
    swapped_data = []

    # Read the existing CSV file
    with open(input_csv, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Skip the header row

        # Swap each row's columns (English to Burmese -> Burmese to English)
        for row in reader:
            english, burmese = row
            swapped_data.append([burmese, english])

    # Step 2: Write the swapped data to a new CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Burmese', 'English'])  # New header after swapping
        writer.writerows(swapped_data)


# Usage Example
swap_csv_columns(covverter_csv, 'swapped_translation.csv')

# Function to load syllable translations from a CSV file into a dictionary
def load_syllable_translations(csv_filename):
    translation_dict = {}
    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present (if any)
        for row in reader:
            if len(row) == 2:  # Ensure the row has exactly 2 columns
                english_syllable, burmese_syllable = row[0].strip(), row[1].strip()
                if english_syllable in translation_dict:
                    translation_dict[english_syllable].append(burmese_syllable)
                else:
                    translation_dict[english_syllable] = [burmese_syllable]
    return translation_dict


# Function to convert an English name to Burmese using the translation dictionary
def convert_name_to_burmese(english_name, translation_dict):
    english_name = capitalize_first_letter(english_name)
    # Split the English name into parts (e.g., "Kaung Htet San" -> ["Kaung", "Htet", "San"])
    name_parts = english_name.split()
    
    # Get all possible translations for each part
    translated_parts = []
    for part in name_parts:
        if part in translation_dict:
            translated_parts.append(translation_dict[part])
        else:
            translated_parts.append([part])  # Use the original part if no translation is found

    # Generate all combinations of the translated parts
    combinations = list(product(*translated_parts))
    
    # Join each combination into a full Burmese name
    burmese_names = [''.join(combo) for combo in combinations]
    
    return burmese_names

# Step 1: Load the syllable translations from the CSV file
translation_dict = load_syllable_translations('swapped_translation.csv')

l1,l2,left, middle, right,r2,r1 = st.columns(7)

# Initialize session state for language selection
if 'left_language' not in st.session_state:
    st.session_state.left_language = 'Burmese'
    st.session_state.right_language = 'English'
    title = 'Burmese Name to English Converter'
    name_title = 'Enter Burmese Name'

# Function to swap languages
def swap_languages():
    
    st.session_state.left_language, st.session_state.right_language = (
        st.session_state.right_language,
        st.session_state.left_language,
    )
    
    
def check_title():
    if st.session_state.left_language == 'Burmese':
        title = 'Burmese Name to English Converter'
    else:
        title = 'English to Burmese Name Converter'
    return title

def check_name_title():
    if st.session_state.left_language == 'Burmese':
        name_title = 'Enter Burmese Name'
    else:
        name_title = 'Enter English Name'
    return name_title

def capitalize_first_letter(text):
    # Convert each word to start with an uppercase letter
    return text.title()

# Button to swap languages
if middle.button("⇆"):
    swap_languages()

# Display current language selection
l1.markdown(f"""<div style='color:orange; padding-top: 5px;'>Change: </div>""", unsafe_allow_html=True)
left.markdown(f"""<div style='color:red; padding-top: 5px;'>{st.session_state.left_language}</div>""", unsafe_allow_html=True)
right.markdown(f"""<div style='color:red; padding-top: 5px;'>{st.session_state.right_language}</div>""", unsafe_allow_html=True)

form = st.form("my_form")
form.markdown(f"""<spam style='font-size:30px; font-weight:bold;'>{check_title()}</spam>""", unsafe_allow_html=True)
name = form.text_input(check_name_title())
button = form.form_submit_button("Convert", type="primary")
form.markdown(":gray[<p style='font-size:12px;'>Copyright © 2024 Hein Htet Arkar Mg</p>]", unsafe_allow_html=True)
if button:
    if st.session_state.left_language == 'Burmese':
        st.markdown(f"""<div ><span style='font-size:16px;'> {check_name_meaning(name, data)}</span></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div style='padding-top:50px;'><span style='color: red; font-size:16px;'>*** Notes: ငသတ်( ် ) ရေးပြီးမှ အောက်ကမြစ်( ့ ) ကိုရေးပါ။ **</span></div>""", unsafe_allow_html=True)
    else:
        output_names = convert_name_to_burmese(name, translation_dict)
        title, ans,blank = st.columns(3)
        title.markdown(f"""<div ><span style='color:orange; font-size:16px;'>Possible Names:</span></div>""", unsafe_allow_html=True)
        for e_name in output_names:
            ans.markdown(f"""<div ><span style='font-size:16px;'> {e_name}</span></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div style='padding-top:50px;'><span style='color: red; font-size:16px;'>*** Notes: English လို Convert ရာတွင် တချို့သော နာမည်များသည် စာလုံးများတူနေသောကြောင့် ဖြစ်နိုင်သောနာမည်များကိုထုတ်ပြပေးထားသည်။ **</span></div>""", unsafe_allow_html=True)
            
        
        
        
