import random
import string

# Define the English and Russian alphabets
english_alphabet = string.ascii_lowercase
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def generate_cipher(alphabet):
    """
    Generate a random cipher for the given alphabet
    """
    cipher = list(alphabet)
    random.shuffle(cipher)
    return ''.join(cipher)

def encode(text, cipher):
    """
    Encode the given text using the given cipher
    """
    encoded_text = ''
    for char in text:
        if char.lower() in english_alphabet:
            index = english_alphabet.index(char.lower())
            if char.isupper():
                encoded_text += cipher[index].upper()
            else:
                encoded_text += cipher[index]
        elif char.lower() in russian_alphabet:
            index = russian_alphabet.index(char.lower())
            if char.isupper():
                encoded_text += cipher[index].upper()
            else:
                encoded_text += cipher[index]
        else:
            encoded_text += char
    return encoded_text

def decode(text, cipher):
    """
    Decode the given text using the given cipher
    """
    decoded_text = ''
    for char in text:
        if char.lower() in english_alphabet:
            index = cipher.index(char.lower())
            if char.isupper():
                decoded_text += english_alphabet[index].upper()
            else:
                decoded_text += english_alphabet[index]
        elif char.lower() in russian_alphabet:
            index = cipher.index(char.lower())
            if char.isupper():
                decoded_text += russian_alphabet[index].upper()
            else:
                decoded_text += russian_alphabet[index]
        else:
            decoded_text += char
    return decoded_text

# Generate a cipher for the English alphabet
english_cipher = generate_cipher(english_alphabet)

# Generate a cipher for the Russian alphabet
russian_cipher = generate_cipher(russian_alphabet)

# Example usage
text = input('напиши текст: ')
encoded_text = encode(text, english_cipher)
decoded_text = decode(encoded_text, english_cipher)
print(encoded_text)
print(decoded_text)

encoded_text = encode(text, russian_cipher)
decoded_text = decode(encoded_text, russian_cipher)
print(encoded_text)
print(decoded_text)