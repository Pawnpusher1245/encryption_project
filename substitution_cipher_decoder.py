import encryption_functions as ef
import json

key_path = 'key.txt'  # Replace with your file path
with open(key_path, 'r') as file:
    letter_mapping = json.load(file)
    key = {v: k for k, v in letter_mapping.items()}

encrypted_file = 'original.txt'
ef.replace_letters_in_file(encrypted_file, key)

