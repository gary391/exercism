def find_anagrams(word, candidates):
    sorted_word = (sorted(word.lower()))
    result = [
        candidate for candidate in candidates if candidate.lower() != word.lower() and     sorted(candidate.lower())==sorted_word
    ]
    return result