import base64
import re

# Caesar Cipher
def caesar(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - start + shift % 26) % 26 + start
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


# Base64
def base(text):
    text_bytes = text.encode("utf-8")
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode("utf-8")


# Vigenere Cipher
def vigenere(text, key):
    s = text.upper()
    k = key.upper()
    # generating the repeated key
    n = ""
    for i in range(len(s)):
        n += k[i % len(k)]
    t = []
    for i in range(len(s)):
        plain_num = ord(s[i]) - ord("A")
        key_num = ord(n[i]) - ord("A")
        cipher_num = (plain_num + key_num) % 26
        t.append(cipher_num)
    # convert numbers to letter
    a = ""
    for x in t:
        a += chr(x + ord("A"))
    return a


# Morse Code
def morse_code(text):
    morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", ".": ".-.-.", ",": "--..--", "?": "..--..",
        "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
        "&": ".-...", ":": "---", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
        "-": "-....-", "_": "..--.-", '"': ".-..-", "$": "...-..-", "@": ".--.-",
        " ": "/",
    }
    morse_result = []
    words = text.upper().split(' ')
    for word in words:
        word_morse = []
        for char in word:
            if char in morse:
                word_morse.append(morse[char])
        if word_morse:
            morse_result.append(" ".join(word_morse))
    return " / ".join(morse_result)


# Reverse
def reverse(text):
    return text[::-1]



# ROTX Cipher
def rotx(text, x):
    result = []
    for char in text:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + x) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + x) % 26 + ord("A") )
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)

# Bifid
def bifid_square(key=""):
    #Generates a 5x5 Bifid square from a key. 'J' is treated as 'I'.
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J is omitted
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    key = re.sub(r'[^A-Z]', '', key)
    square_str = key + "".join([c for c in alphabet if c not in key])
    square = {}
    reverse_square = {}
    for i, char in enumerate(square_str):
        row, col = divmod(i, 5)
        square[char] = (row + 1, col + 1)
        reverse_square[(row + 1, col + 1)] = char
        
    return square, reverse_square

def bifid(text, key: str = "", encrypt: bool = True):
    square, reverse_square = bifid_square(key)
    text = text.upper().replace('J', 'I')
    text = re.sub(r'[^A-Z]', '', text)

    if not text:
        return ""
    
    if encrypt:
        coords = [square[char] for char in text]
        rows = [coord[0] for coord in coords]
        cols = [coord[1] for coord in coords]
        all_coords = rows + cols
        
        ciphertext = ""
        for i in range(0, len(all_coords), 2):
            new_coord = (all_coords[i], all_coords[i+1])
            ciphertext += reverse_square[new_coord]
        return ciphertext
   
