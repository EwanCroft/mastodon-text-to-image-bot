import json
import string
import secrets
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(ROOT_DIR, 'sorted_chars.json')

dictionary_of_colours = {}

for char in string.printable:
    hex_code = secrets.token_hex(3)
    dictionary_of_colours[char] = hex_code

sorted_chars = [char for char in string.printable]
sorted_colours = sorted(dictionary_of_colours.items(), key=lambda x: x[1])
sorted_data = {char: colour for char, colour in sorted_colours}

with open(JSON_FILE, 'w') as f:
    json.dump(sorted_data, f, indent=4)

print(f'Sorted data has been written to {JSON_FILE}')
