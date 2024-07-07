def parse_fasta(lines) -> list:
    sequences = []
    seq = ""
    seq_id = ""
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if seq:
                sequences.append((seq_id, seq))
                seq = ""
            seq_id = line[1:]
        else:
            seq += line
    if seq:
        sequences.append((seq_id, seq))

    return sequences

def calculate_gc_percentage(seq):
    g_count = seq.count("G")
    c_count = seq.count("C")
    gc_content = g_count + c_count

    return gc_content / len(seq) * 100

with open("bioinformatics_stronghold/t.txt", "r") as file:
    lines = file.readlines()

sequences = parse_fasta(lines)

largest_gc_content = 0
largest_gc_id = ""

for seq_id, seq in sequences:
    percentage = calculate_gc_percentage(seq)
    if percentage > largest_gc_content:
        largest_gc_content = percentage
        largest_gc_id = seq_id

print(largest_gc_id)
print(largest_gc_content)