import encryption_functions as ef

def add_letters(a, b):
    """Adds letters (mod 26), where counting starts from 0"""
    ascii_a = ord(a) - ord('a')
    ascii_b = ord(b) - ord('a')

    result = (ascii_a + ascii_b) % 26

    return chr(result + ord('a'))

file_path = 'original.txt'
key_path = 'key.txt'
encrypted_file_path = 'modified.txt'

index_tracker = 0
encrypted_text = ""
key = 'abaaaaaaaaaaa'
length_of_key = len(key)

# Makes everything lowercase to ensure that the shifting is correct
ef.make_lower(file_path)

# Stores the key in the file 'key.txt'.
with open(key_path, 'w', encoding = 'utf-8') as file:
      file.write(key)

with open(file_path, 'r', encoding = 'utf-8') as file:
        file_content = file.read()

# Makes an encrypted version according to the vigenere cipher.
for character in file_content:
      if character.isalpha():
            index_tracker %= length_of_key
            letter_to_add = key[index_tracker]
            encrypted_text += add_letters(character, letter_to_add)
            index_tracker += 1
      else:
            encrypted_text += character

# Stores the encrypted file.
with open(encrypted_file_path, 'w', encoding = 'utf-8') as file:
      file.write(encrypted_text)
