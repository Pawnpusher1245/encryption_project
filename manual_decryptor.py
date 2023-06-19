import re

def bf_replace_individual_letters_in_file(original_file, modified_file, replacement_mapping):
    """
    Replaces individual letters in an original file with corresponding letters based on the provided mapping.
    
    Args:
        original_file (str): The path to the original file.
        modified_file (str): The path to the modified file where the replaced text will be stored.
        replacement_mapping (dict): A dictionary containing the mapping of old letters to new letters.

    Raises:
        FileNotFoundError: If the original file is not found.
        Exception: If any other error occurs during the replacement process.

    """
    try:
        with open(original_file, 'r') as file:
            original_text = file.read()

        modified_text = original_text

        pattern = '|'.join(replacement_mapping.keys())
        modified_text = re.sub(pattern, lambda match: replacement_mapping[match.group(0)], modified_text)

        with open(modified_file, 'w') as file:
            file.write(modified_text)

        print("Replacement completed successfully. Modified file created.")

    except FileNotFoundError:
        print("Original file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


replacement_mapping = {
    'l' : 'h',
    'i' : 'n',
    'o' : 'i',
    'h' : 's',
    's' : 'o'
}

bf_replace_individual_letters_in_file('original.txt', 'modified.txt', replacement_mapping)
