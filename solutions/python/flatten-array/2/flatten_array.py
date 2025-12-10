def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            # recursive step:
            # 1. call flatten on item
            # 2. add all returned elements into result
            result.extend(flatten(item))
        else:
            # base case:
            # just append item to result
            if item is not None:
                result.append(item)
    return result
