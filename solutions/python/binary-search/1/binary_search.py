def find(search_list, value):
    return _find(search_list, value, 0, len(search_list) - 1)


def _find(search_list, value, low, high):

    # 1. base case: if low > high → value not found
    # 2. compute mid = (low + high) // 2
    # 3. if search_list[mid] == value → return mid
    # 4. if search_list[mid] < value → recurse on right half (mid+1 .. high)
    # 5. if search_list[mid] > value → recurse on left half (low .. mid-1)
    if low > high:
        raise ValueError("value not in array")
    mid = (low + high) // 2
    if search_list[mid] == value:
        return mid
    elif search_list[mid] < value:
        return _find(search_list, value, mid+1, high)
    elif search_list[mid] > value:
        return _find(search_list, value, low, mid-1)