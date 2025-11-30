# def to_rna(dna_strand):
    
#     rna_strand = ""
#     for items in dna_strand:
#         if items == "T":
#             rna_strand = rna_strand + "A"
#         elif items == "C":
#             rna_strand = rna_strand + "G"
#         elif items == "G":
#             rna_strand = rna_strand + "C"
#         elif items == "A":
#             rna_strand = rna_strand + "U"
#     return rna_strand

TRANSLATE = {"T": "A", "C": "G", "G": "C", "A": "U"}

def to_rna(dna_strand):
    return "".join(TRANSLATE[item] for item in dna_strand)