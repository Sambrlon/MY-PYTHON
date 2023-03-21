# Define dictionaries that map each letter to a corresponding code letter for the English and Russian alphabets
english_code_map = {'a': 'x', 'b': 'z', 'c': 'p', 'd': 'q', 'e': 'm', 'f': 'k', 'g': 'l', 'h': 'j', 'i': 'n', 'j': 'h',
                    'k': 'f', 'l': 'g', 'm': 'e', 'n': 'i', 'o': 'r', 'p': 'c', 'q': 'd', 'r': 'o', 's': 'u', 't': 'v',
                    'u': 's', 'v': 't', 'w': 'y', 'x': 'a', 'y': 'w', 'z': 'b'}
russian_code_map = {'а': 'ъ', 'б': 'я', 'в': 'ч', 'г': 'ж', 'д': 'э', 'е': 'м', 'ё': 'т', 'ж': 'д', 'з': 'в', 'и': 'н',
                    'й': 'г', 'к': 'й', 'л': 'к', 'м': 'е', 'н': 'и', 'о': 'р', 'п': 'ц', 'р': 'о', 'с': 'у', 'т': 'ы',
                    'у': 'с', 'ф': 'щ', 'х': 'ш', 'ц': 'з', 'ч': 'ф', 'ш': 'х', 'щ': 'ъ', 'ъ': 'ь', 'ы': 'б', 'ь': 'ю',
                    'э': 'э', 'ю': 'п', 'я': 'а'}

# Define a function that generates a coded message
def generate_code(message, code_map):
    # Convert the message to lowercase
    message = message.lower()

    # Generate the coded message
    coded_message = ''
    for letter in message:
        if letter in code_map:
            coded_letter = code_map[letter]
        else:
            coded_letter = letter
        coded_message += coded_letter

    return coded_message

# Define a function that decodes a message step by step
def decode_text(coded_message, code_map):
    # Convert the coded message to lowercase
    coded_message = coded_message.lower()

    # Decode the message step by step
    decoded_message = ''
    for i in range(len(coded_message)):
        if coded_message[i] in code_map:
            decoded_letter = code_map[coded_message[i]]
        else:
            decoded_letter = coded_message[i]
        decoded_message += decoded_letter
        print(f"Step {i + 1}: {decoded_message}")

    return decoded_message

# Example usage for coding
english_message = "Hello, world!"
russian_message = "Привет, мир!"
english_coded_message = generate_code(english_message, english_code_map)
russian_coded_message = generate_code(russian_message, russian_code_map)
print(f"Coded English message: {english_coded_message}")
print(f"Coded Russian message: {russian_coded_message}")

english_decoded_message = decode_text(english_coded_message, english_code_map)
russian_decoded_message = decode_text(russian_coded_message, russian_code_map)
print(f"Decoded English message: {english_decoded_message}")
print(f"Decoded Russian message: {russian_decoded_message}")
