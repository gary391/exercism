
def find(search_list, value):
    b = 0
    e = len(search_list) -1
    while b <= e:
        m = (b + e) // 2
        if search_list[m] < value:
            b = m + 1
        else:
            e = m - 1

    if b == len(search_list) or search_list[b] != value:
        raise ValueError("value not in array")
    else:
        return b
