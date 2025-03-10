# Immutable alphabet for decoders/encoders to check against.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Function for decoding Caesar Ciphers with known shift factor.
def caesar_decoder(coded_message, shift_factor):
    decoded_message = []
    for letter in coded_message:
        alpha_position = 0
        caesar_letter = ""
        caesar_position = 0
        overflow_caesar_position = 0
        if letter in alphabet:
            alpha_position = alphabet.index(letter)
            caesar_position = alpha_position + shift_factor
            if caesar_position > 25:
                overflow_caesar_position = caesar_position % 26
                caesar_letter = alphabet[overflow_caesar_position]
            else:
                caesar_letter = alphabet[caesar_position]
            decoded_message.append(caesar_letter)
        else:
            decoded_message.append(letter)
    readout = "".join(decoded_message)
    print(readout)

# Function for encoding Caesar Ciphers with provided shift factor.
def caesar_encoder(raw_message, shift_factor):
    encoded_message = []
    for letter in raw_message:
        alpha_position = 0
        caesar_letter = ""
        caesar_position = 0
        overflow_caesar_position = 0
        if letter in alphabet:
            alpha_position = alphabet.index(letter)
            caesar_position = alpha_position - shift_factor
            if caesar_position < 0:
                overflow_caesar_position = caesar_position % -26
                caesar_letter = alphabet[overflow_caesar_position]
            else:
                caesar_letter = alphabet[caesar_position]
            encoded_message.append(caesar_letter)
        else:
            encoded_message.append(letter)
    readout = "".join(encoded_message)
    print(readout)

# Function for iterating the decoder where "difficulty" is the number of iterations.
# Each iteration needs visually inspecting in the output to verify legibility.
def caesar_brute_force(coded_message, difficulty):
    for x in range(difficulty):
        print("Shift ", x)
        caesar_decoder(coded_message, x)

# Function for decoding Vigenère Ciphers with known keyword.
def vigenere_decoder(coded_message, key):
    decoded_message = []
    place = 0
    for letter in coded_message:
        alpha_position = 0
        key_position = 0
        vigenere_letter = ""
        if letter in alphabet:
            alpha_position = alphabet.index(letter)
            key_position = alphabet.index(key[place % len(key)])
            vigenere_letter = alphabet[(alpha_position + key_position) % 26]
            decoded_message.append(vigenere_letter)
            place += 1
        else:
            decoded_message.append(letter)
    readout = "".join(decoded_message)
    print(readout)

# Function for encoding Vigenère Ciphers with provided keyword.
def vigenere_encoder(raw_message, key):
    encoded_message = []
    place = 0
    for letter in raw_message:
        alpha_position = 0
        key_position = 0
        vigenere_letter = ""
        if letter in alphabet:
            alpha_position = alphabet.index(letter)
            key_position = alphabet.index(key[place % len(key)])
            vigenere_letter = alphabet[(alpha_position - key_position) % 26]
            encoded_message.append(vigenere_letter)
            place += 1
        else:
            encoded_message.append(letter)
    readout = "".join(encoded_message)
    print(readout)