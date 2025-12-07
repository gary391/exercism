def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    return  sum(elem_a != elem_b for elem_a, elem_b in zip(strand_a, strand_b))