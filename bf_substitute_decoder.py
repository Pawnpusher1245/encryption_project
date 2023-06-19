import encryption_functions as ef

frequency_letters = [
    'e', 't', 'a', 'o', 'i', 'n', 's',
    'h', 'r', 'd', 'l', 'c', 'u', 'm',
    'w', 'f', 'g', 'y', 'p', 'b', 'v',
    'k', 'j', 'x', 'q', 'z'
]
i = 0

file_path = 'original.txt'

sorted_letters = ef.count_frequency_letters(file_path)  # Replace with your file path
frequency_mapping = {}

for letter, _ in sorted_letters:
    frequency_mapping[letter] = frequency_letters[i]
    i += 1
    
ef.replace_letters_in_file(file_path, frequency_mapping)