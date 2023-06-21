def subtract_letters(value, encrpytion_key):
    """Subtracts letters (mod 26), where counting starts from 0"""
    ascii_a = ord(value) - ord('a')
    ascii_b = ord(encrpytion_key) - ord('a')

    result = (ascii_a - ascii_b) % 26

    return chr(result + ord('a'))

key_path = 'key.txt'
encrypted_path = 'modified.txt' 

# Opens the key from the file 'key.txt'.
with open(key_path, 'r', encoding = 'utf-8') as file:
      key = file.read()

length_of_key = len(key)

with open(encrypted_path, 'r', encoding = 'utf-8') as file:
      file_content = file.read()

index_tracker = 0
decrypted_text = ""

for character in file_content:
      if character.isalpha():
            index_tracker %= length_of_key
            letter_to_subtract = key[index_tracker]
            decrypted_text += subtract_letters(character, letter_to_subtract)
            index_tracker += 1
      else:
            decrypted_text += character

with open(encrypted_path, 'w', encoding = 'utf-8') as file:
      file.write(decrypted_text)