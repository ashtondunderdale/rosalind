genetic_code = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "CAU": "H", "CAC": "H",
    "AAU": "N", "AAC": "N", "GAU": "D", "GAC": "D",
    "UAA": "Stop", "UAG": "Stop", "UGA": "Stop",
    "CAA": "Q", "CAG": "Q", "AAA": "K", "AAG": "K",
    "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "UGG": "W"
}

with open("bioinformatics_stronghold/rna_splicing.txt") as file:
    lines = file.read().split(">")[1:]
    dna = lines[0].split('\n', 1)[1].replace('\n', '')
    introns = ["".join(line.split('\n')[1:]) for line in lines[1:]]

for intron in introns:
    dna = dna.replace(intron, "")

rna = dna.replace("T", "U")
protein = "".join(genetic_code[rna[i:i+3]] for i in range(0, len(rna), 3) if genetic_code[rna[i:i+3]] != "Stop")

print(protein)