import Encoder
from Gui import InputDialog
import pyperclip


def compute():
    # Launch gui
    val = InputDialog()

    crypto = val.select  # selected cipher
    plaintext = val.result  # plain entered
    key = val.key_value  # optional key

    if crypto == "Caesar Cipher" or crypto == "ROT":
        shift = int(key) if key else 0
        cipher = Encoder.caesar(plaintext, shift)
    elif crypto == "Base64":
        cipher = Encoder.base(plaintext)
    elif crypto == "Vigenere Cipher(dCode)":
        cipher = Encoder.vigenere(plaintext, key)
    elif crypto == "Morse Code":
        cipher = Encoder.morse_code(plaintext)
    elif crypto == "Reverse":
        cipher = Encoder.reverse(plaintext)
    elif crypto == "Bifid":
        cipher = Encoder.bifid(plaintext, key)
    else:
        cipher = plaintext  # fallback

    return cipher


if __name__ == "__main__":
    output = compute()
    pyperclip.copy(output)
    print("Copied to clipboard:", output)
