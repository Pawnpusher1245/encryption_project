
import json
import encryption_functions as ef


# Create a random letter mapping for lowercase letters
letter_mapping = ef.create_random_mapping()

file_path = 'original.txt'

ef.make_lower(file_path)

ef.replace_letters_in_file(file_path, letter_mapping)


# Convert the dictionary to a JSON string
json_data = json.dumps(letter_mapping)

# Open the file in write mode and write the JSON data
with open('key.txt', 'w', encoding='utf-8') as file:
    file.write(json_data)