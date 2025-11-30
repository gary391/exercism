def to_rna(dna_strand):
    
    rna_strand = ""
    for items in dna_strand:
        if items == "T":
            rna_strand = rna_strand + "A"
        elif items == "C":
            rna_strand = rna_strand + "G"
        elif items == "G":
            rna_strand = rna_strand + "C"
        elif items == "A":
            rna_strand = rna_strand + "U"
        else:
            rna_strand = rna_strand + items
    return rna_strand
