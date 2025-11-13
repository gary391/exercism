import string

def is_pangram(sentence):
    lowercase_alphabet = string.ascii_lowercase
    return set(lowercase_alphabet).issubset(set(sentence.lower()))
        
    
    
