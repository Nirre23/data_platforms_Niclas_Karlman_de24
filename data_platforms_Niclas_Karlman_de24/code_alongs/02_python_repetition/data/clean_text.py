import re

with open("data/ml_text_raw.txt", 'r') as file:
    raw_text = file.read()

test_fixed_spacing = re.sub(r"\s+"," ",raw_text) 
test_fixed_spacing 
