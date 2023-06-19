import random
import string
from collections import Counter
import unicodedata

def create_random_mapping():
    """
    Creates a random mapping dictionary where each lowercase letter is mapped to another randomly shuffled letter.
    Returns:
        mapping (dict): A dictionary containing the random letter mapping.
    """
    lowercase_letters = string.ascii_lowercase
    shuffled_letters = random.sample(lowercase_letters, len(lowercase_letters))
    mapping = {}
    for i in range(len(lowercase_letters)):
        mapping[lowercase_letters[i]] = shuffled_letters[i]
    return mapping

def apply_mapping(text, mapping):
    """
    Applies the given mapping dictionary to the provided text and replaces each occurrence of a letter with its mapped value.
    Args:
        text (str): The text to apply the mapping to.
        mapping (dict): A dictionary containing the letter mapping.
    Returns:
        result (str): The text with the letter mapping applied.
    """
    result = ""
    for letter in text:
        if letter in mapping:
            result += mapping[letter]
        else:
            result += letter
    return result

def replace_letters_in_file(filename, mapping):
    """
    Replaces the letters in the specified file according to the provided mapping.
    Args:
        filename (str): The path to the file.
        mapping (dict): A dictionary containing the letter mapping.
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        text = file.read()
        encrypted_text = apply_mapping(text, mapping)
        file.seek(0)
        file.write(encrypted_text)
        file.truncate()

def make_lower(file_path):
    """
    Converts all characters in the specified file to lowercase.
    Args:
        file_path (str): The path to the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        lowercase_text = text.lower()

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(lowercase_text)

def count_frequency_letters(file_path):
    """
    Counts the frequency of lowercase letters in the specified file.
    Args:
        file_path (str): The path to the file.
    Returns:
        sorted_letters (list): A list of tuples containing lowercase letters and their corresponding frequencies, sorted by frequency in descending order.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    normalized_content = unicodedata.normalize('NFKD', content)
    content = ''.join([char.lower() for char in normalized_content if unicodedata.category(char) == 'Ll'])

    letter_count = Counter(content)
    sorted_letters = sorted(letter_count.items(), key=lambda pair: pair[1], reverse=True)

    return sorted_letters
