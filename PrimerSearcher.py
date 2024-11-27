def find_gc_sequence(dna_string):
    target_length = 20
    target_gc_count = 11

    for i in range(len(dna_string) - target_length + 1):
        sequence = dna_string[i:i + target_length]
        gc_count = sequence.count('G') + sequence.count('C')
        if gc_count == target_gc_count:
            return sequence

    return None

dna_string = """ATGGCGTTAAATCACACTGCCCTGCCTCAGGACGAGCGCCTGCCCCATTA
CCTTCGAGATGGGGATCCTTTTGCTTCCAAACTTTCTTGGGAAGCGGATT
TAGTGGCTGGCTTTTACCTAACAATAATTGGGATTCTGTCCACATTTGGA
AATGGATATGTCCTTTACATGTCTTCTAGACGAAAGAAGAAGCTGAGACC
CGCTGAAATAATGACTATCAATTTAGCAGTCTGTGATCTGGGGATTTCAG
TTGTAGGCAAGCCGTTCACCATCATCTCTTGCTTTTGTCACCGCTGGGTG
TTTGGCTGGATCGGCTGCCGCTGGTATGGATGGGCTGGATTTTTCTTTGG
CTGTGGAAGCCTTATCACCATGACTGCTGTCAGCCTGGATCGATATTTGA
AAATCTGCTATTTATCTTATGGGGTTTGGCTGAAAAGAAAGCACGCCTAC
ATCTGCCTGGCAGCCATCTGGGCCTATGCTTCCTTCTGGACCACCATGCC
CTTGGTAGGTCTGGGGGACTACGTACCTGAGCCCTTCGGAACCTCGTGCA
CCCTGGACTGGTGGCTGGCCCAGGCCTCGGTAGGGGGCCAGGTTTTCATC
CTGAACATCCTCTTCTTCTGCCTCTTGCTCCCAACGGCTGTGATCGTGTT
CTCCTACGTAAAGATCATTGCCAAGGTTAAGTCCTCTTCCAAAGAAGTAG
CTCATTTCGACAGTCGGATCCATAGCAGCCATGTGCTGGAAATGAAACTG
ACAAAGGTAGCGATGTTGATTTGTGCTGGATTCCTGATTGCCTGGATTCC
TTATGCAGTGGTGTCTGTGTGGTCAGCTTTTGGAAGGCCAGACTCCATTC
CCATACAGCTCTCTGTGGTGCCAACCCTACTTGCAAAATCTGCAGCGATG
TACAATCCCATCATTTACCAAGTTATTGATTACAAATTTGCCTGTTGCCA
AACTGGTGGTTTGAAAGCAACCAAGAAGAAGTCTCTGGAAGGCTTCAGGC
TGCACACCGTAACCACAGTCAGGAAGTCTTCTGCTGTGCTGGAAATTCAT
GAAGAGTGGGAATAA"""
dna_string = dna_string.replace("\n", "")


all_results = []
start = 0

while start < len(dna_string) - 20 + 1:
    result = find_gc_sequence(dna_string[start:])
    if result:
        all_results.append(result)
        start += dna_string[start:].index(result) + 1
        if not (result.startswith('GC') or (result.endswith('GC') )):
            all_results.pop()
    else:
        break

if all_results:
    filtered_results = []
    invalid_start_ends = ["GCC","GCG","GGC","CGG","CCG","CGC"]
    for i in range(len(all_results)):
        seq = all_results[i]
        if (not (("TTTT" in seq or "AAAA" in seq or "CCCC" in seq or "GGGG" in seq)
            or (seq[-3:] in invalid_start_ends or seq[:3] in invalid_start_ends))):
            filtered_results.append(seq)

    for i in range(len(filtered_results)):
        seq = filtered_results[i]
        if seq.startswith('GC'):
            print(f"{i + 1}. Found sequence: (R) {seq}")
        elif seq.endswith('GC'):
            print(f"{i + 1}. Found sequence: (F) {seq}")
        else:
            print("Warning: doesn't start with or end with GC")
else:
    print("No sequence found")