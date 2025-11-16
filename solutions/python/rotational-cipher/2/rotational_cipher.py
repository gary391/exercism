def rotate(text, key):
    encrypted_text = ""
    for letter in text:
        if letter.islower():
            encrypted_letter = chr((ord(letter) + key-97) % 26 + 97)
            encrypted_text = encrypted_text + encrypted_letter
        elif letter.isupper():
            encrypted_letter = chr((ord(letter) + key-65) % 26 + 65)
            encrypted_text = encrypted_text + encrypted_letter
        else:
            encrypted_text = encrypted_text + letter
    return encrypted_text