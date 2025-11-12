
import string

def is_pangram(sentence):
    set_sent = set()
    lowercase_alphabet = string.ascii_lowercase
    for letter in sentence:
        lower_letter = letter.lower()
        if lower_letter in lowercase_alphabet:  # all lowercase
            set_sent.add(lower_letter)
    return set_sent == set(lowercase_alphabet)
        
        
    
    
