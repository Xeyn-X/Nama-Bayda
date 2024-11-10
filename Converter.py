import streamlit as st
import csv
import re
import pandas as pd
from itertools import product


# Function to load data from a CSV file
def load_csv_data(file_path):
    data_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns (Name, Meaning)
                    data_dict[row[0].strip()] = row[1].strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading '{file_path}': {e}")
    return data_dict

# Function to check for special name combinations
def check_special_name(name):
    syllables = name.split()  # Split name into individual words
    result = []
    i = 0
    while i < len(syllables):
        # Check if a combination of the current and next syllable exists in special_name
        if i < len(syllables) - 2:
            combined_syllable = syllables[i] + " "+ syllables[i + 1] + " " + syllables[i + 2]  # Combine three syllables
            if combined_syllable in special_name:
                result.append(special_name[combined_syllable])
                i += 3  # Skip the next two syllables as they are part of the special name
                continue
        # Check for combined syllables (two-word combinations)
        if i < len(syllables) - 1:
            combined_syllable = syllables[i] + " " + syllables[i + 1]
            if combined_syllable in special_name:
                result.append(special_name[combined_syllable])
                i += 2  # Skip the next syllable since it's matched
                continue
        # If no match, add the current syllable as is
        result.append(syllables[i])
        i += 1
    return " ".join(result)

# Function to check the meaning of each part of the name
def check_name_meaning(name):
    #Apply the function to the name
    swap_name = swap_characters(name)
    # Split Burmese name into syllables using regex
    name_syllable = re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))', r' \1', swap_name)
    name_syllable = check_special_name(name_syllable)

    # Split the processed name into parts
    name_parts = name_syllable.split()
    meanings = []  # List to store meanings

    # Check for meanings in the CSV data
    for part in name_parts:
        if part in data:
            meanings.append(data[part])
        else:
            meanings.append(f"({part})")  # Indicate no meaning found

    # Join the meanings into a single string
    result = " ".join(meanings) if meanings else "(None)"
    return result

# Define a function to swap
def swap_characters(name):
    swap_name_list = {'ယဉ်':'ယဥ်','သဉ္ဇာ':'သဥ္ဇာ','မဥ္ဇူ':'မဥ္ဇူ',}
    # Check if the name contains any exceptions, if so, return it as is
    for key, value in swap_name_list.items():
        if key in name:
            # Replace key with value directly (preserving exceptions)
            name = name.replace(key, value)
    # Using re.sub() to find the pattern and swap it
    # Swap 'ဦး' -> 'ဦ်း'
    # Unicode sequence: \u1026\u1038\u103a to \u1026\u103a\u1038
    swapped_name = re.sub(r'\u1026\u1038', '\u1025\u102e\u1038', name)


    # '\u1037\u103a' represents '့ ်'
    # '\u103a\u1037' represents '်  ့'
    swapped_name = re.sub(r'(\u1037)(\u103a)', r'\2\1', swapped_name)
    return swapped_name

# Function to load names from an uploaded CSV file
def load_names_from_csv(uploaded_file):
    names_list = []
    try:
        # Check if a file is uploaded
        if uploaded_file is not None:
            reader = csv.reader(uploaded_file.read().decode('utf-8').splitlines())
            next(reader)  # Skip header row if needed
            for row in reader:
                if row:  # Ensure there is at least one column (Name)
                    names_list.append(row[0].strip())
    except Exception as e:
        st.error(f"Error reading uploaded file: {e}")
    return names_list

# Load data from CSV files
coverter_csv = '/Users/heinhtetarkarmg/Downloads/Converter.csv'
data = load_csv_data(coverter_csv)
special_name = load_csv_data('/Users/heinhtetarkarmg/Downloads/SpecialName.csv')


#English to Burmese
# Load the existing CSV file and swap columns
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
    
# Usage Example
swap_csv_columns(coverter_csv, 'swapped_translation.csv')

# Load the syllable translations from the CSV file
translation_dict = load_syllable_translations('swapped_translation.csv')


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
    

l1,l2,left, middle, right,r2,r1 = st.columns(7)
# Button to swap languages
if r2.button("⇆"):
    swap_languages()

# Display current language selection
left.markdown(f"""<div style='color:orange; padding-top: 5px;'>Change: </div>""", unsafe_allow_html=True)
right.markdown(f"""<div style='color:red; padding-top: 5px;'>{st.session_state.left_language}</div>""", unsafe_allow_html=True)
r1.markdown(f"""<div style='color:red; padding-top: 5px;'>{st.session_state.right_language}</div>""", unsafe_allow_html=True)
st.divider()
st.markdown(f"""<spam style='font-size:30px; font-weight:bold;'>{check_title()}</spam>""", unsafe_allow_html=True)
name = st.text_input(check_name_title())

# Convert input string to a list
name = [item.strip() for item in name.split(',') if item]


if st.session_state.left_language == 'Burmese':
    st.markdown("<p style='text-align:center; font-size:20px; color:orange;'>Or</p>", unsafe_allow_html=True)
    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        name = load_names_from_csv(uploaded_file)
        
        
        
con,mid,dwn = st.columns(3)
button = con.button("Convert", type="primary")


st.markdown(":gray[<p style='font-size:12px;'>Copyright © 2024 Hein Htet Arkar Mg</p>]", unsafe_allow_html=True)
st.divider()
if button:
    if st.session_state.left_language == 'Burmese':
        output=[]
        for out in name:
            output.append(check_name_meaning(out))
            st.markdown(f"""<div ><span style='font-size:16px;'> {check_name_meaning(out)}</span></div>""", unsafe_allow_html=True)

        # Convert output list to a DataFrame
        df = pd.DataFrame(output, columns=["Names"])
        
        # Save DataFrame to CSV and provide a download button
        csv_data = df.to_csv(index=False)
        
        # Use Streamlit's download button to save the file
        dwn.download_button(
            label="Download CSV",
            data=csv_data,
            file_name='BurmeseToEnglishNameConvert.csv',
            mime='text/csv'
        )
    else:
        output_names = convert_name_to_burmese(name, translation_dict)
        title, ans,blank = st.columns(3)
        title.markdown(f"""<div ><span style='color:orange; font-size:16px;'>Possible Names:</span></div>""", unsafe_allow_html=True)
        for e_name in output_names:
            ans.markdown(f"""<div ><span style='font-size:16px;'> {e_name}</span></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div ><span style='color: red; font-size:16px;'>*** Notes: English လို Convert ရာတွင် တချို့သော နာမည်များသည် စာလုံးများတူနေသောကြောင့် ဖြစ်နိုင်သောနာမည်များကိုထုတ်ပြပေးထားသည်။ **</span></div>""", unsafe_allow_html=True)
            
        
        
        