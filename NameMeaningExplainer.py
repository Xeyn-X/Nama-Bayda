import re
from re import search
import json
import streamlit as st

# Function to check the meaning of each part of the name
def check_name_meaning(name, data):
    name_syllable = re.sub(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))', r' \1', name)
    
    # Split the Burmese name by each word
    name_parts = name_syllable.split()
    meanings = []  # List to store meanings

     # Loop through each part of the name and check if it exists in the data
    for part in part_data:
        if search(part, name):  # Check if part is found in the name using regex search
            if part_data[part] not in meanings:  # Add meaning if not a duplicate
                meanings.append(part_data[part])
                
    # Loop through each part of the name
    for part in name_parts:
        if part in data:  # Check if part has a meaning in the dictionary
            if data[part] not in meanings:  # Add meaning if not a duplicate
                meanings.append(data[part])
       
    # Format the result as a comma-separated string
    result = f"{', '.join(meanings)}" if meanings else "(None)"
    return result
        
# Load data from JSON file
with open('./Burmese_Name_Meaning.json', 'r', encoding='utf-8') as file:
    meaning_data = json.load(file)
    
part_data = {
    'မြင့်မြတ်': 'Noble',
    'သူရိန်': 'Sun',
    'သူရ': 'Bravery',
    'စိုးမိုး': 'Power',
    'သီဟ': 'lion',
    'သီရိ': 'Glory',
    'သီတာ': 'Royal Princess',
    'ဇာနည်': 'Bravery',
    'ဇာခြည်': 'Sunlight',
    'သဇင်': 'Royal Flower',
    'သခင်': 'Master',
    'မာလာ': 'Necklace of Flower',
    'နီလာ': 'Sapphire',
    'ယမင်း': 'Princess',
    'ယမုံ': 'Feminine',
    'ဝတ်ရည်': 'Nectar',
    'ဝတ်မှုံ': 'Pollen',
    'ဝတ်လွှာ': 'Petal',
    'လမင်း': 'Moon',
    'လပြည့်': 'Moon',
    'လဝန်း': 'Moon',
    'ဝေယံ': 'Sky',
    'ဇေယျာ': 'Victory',
    'ဇေယျ': 'Victory',
    'နေခြည်': 'Sun light',
    'စည်သူ': 'Honorable',
    'ဟေမန်': 'Winter',
    'ရတနာ': 'Treasure',
    'အာကာ': 'Space',
    'ချယ်ရီ': 'Cherry',
    'သုခ': 'Pleasure',
    'သုတ': 'Wisdom',
    'ကလျာ': 'Womanly virtues',
    'အင်ကြင်း': 'Sal tree',
    'စံပယ်': 'Jasmine',
    'ငုဝါ': 'Flower',
    'ဗညား': 'Royal',
    'ဂျူလိုင်': 'July',
    'ဇူလိုင်': 'July',
    'ဝသုန်': 'Earth',
    'ဝသန်': 'Rain',
    'ဆည်းဆာ': 'Sunset',
    'ပုလဲ': 'Pearl',
    'ကံ့ကော်': 'Flower',
    'တိမ်လွှာ': 'Cloud',
    'ပတ္တမြား': 'Ruby',
    'ရာဇာ': 'King',
    'ဧကရီ': 'Queen',
}

form = st.form("my_form")
form.markdown("<spam style='font-size:30px; font-weight:bold;'>Name Meaning Explainer</spam><spam style='font-size:15px; font-weight:bold; color: gray;'> for Burmese</spam>", unsafe_allow_html=True)
name = form.text_input("Enter Burmese Name")
button = form.form_submit_button("Definition", type="primary")
form.markdown(":gray[<p style='font-size:12px;'>Copyright © 2024 Hein Htet Arkar Mg</p>]", unsafe_allow_html=True)
if button:
    st.write(check_name_meaning(name, meaning_data))
