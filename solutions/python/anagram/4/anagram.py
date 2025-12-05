def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    word_lower = word.lower()
    return [
        candidate for candidate in candidates
        if candidate.lower() != word_lower and  
        sorted(candidate.lower())==sorted_word
    ]