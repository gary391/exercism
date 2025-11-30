TRANSLATE = {"T": "A", "C": "G", "G": "C", "A": "U"}

def to_rna(dna_strand):
    return "".join(TRANSLATE[item] for item in dna_strand)