def is_isogram(orig_string):
    str_count = {}
    string = orig_string.lower()
    for char in string:
        if not char.isalpha():
            continue
        if char not in str_count:
            str_count[char] = 1
        else:
            str_count[char] += 1
    if any(value > 1 for value in str_count.values()) :
        return False
    return True