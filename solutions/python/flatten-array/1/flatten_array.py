def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            new_list = flatten(item)
            # recursive step:
            # 1. call flatten on item
            # 2. add all returned elements into result
            result += new_list
        else:
            # base case:
            # 1. just append item to result
            if item is not None:
                result.append(item)
    return result
