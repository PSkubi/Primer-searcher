def find_gc_sequence(dna_string):
    target_length = 20
    target_gc_count = 10

    for i in range(len(dna_string) - target_length + 1):
        sequence = dna_string[i:i + target_length]
        gc_count = sequence.count('G') + sequence.count('C')
        if gc_count == target_gc_count or gc_count == target_gc_count+1:
            return sequence

    return None

dna_string = "ATGTACTCGGGGAACCGCAGCGGCGGCCACGGCTACTGGGACGGCGGCGG GGCCGCGGGCGCTGAGGGGCCGGCGCCGGCGGGGACACTGAGCCCCGCGC CCCTCTTCAGCCCCGGCACCTACGAGCGCCTGGCGCTGCTGCTGGGCTCC ATTGGGCTGCTGGGCGTCGGCAACAACCTGCTGGTGCTCGTCCTCTACTA CAAGTTCCAGCGGCTCCGCACTCCCACTCACCTCCTCCTGGTCAACATCA GCCTCAGCGACCTGCTGGTGTCCCTCTTCGGGGTCACCTTTACCTTCGTG TCCTGCCTGAGGAACGGCTGGGTGTGGGACACCGTGGGCTGCGTGTGGGA CGGGTTTAGCGGCAGCCTCTTCGGGATTGTTTCCATTGCCACCCTAACCG TGCTGGCCTATGAACGTTACATTCGCGTGGTCCATGCCAGAGTGATCAAT TTTTCCTGGGCCTGGAGGGCCATTACCTACATCTGGCTCTACTCACTGGC GTGGGCAGGAGCACCTCTCCTGGGATGGAACAGGTACATCCTGGACGTAC ACGGACTAGGCTGCACTGTGGACTGGAAATCCAAGGATGCCAACGATTCC TCCTTTGTGCTTTTCTTATTTCTTGGCTGCCTGGTGGTGCCCCTGGGTGT CATAGCCCATTGCTATGGCCATATTCTATATTCCATTCGAATGCTTCGTT GTGTGGAAGATCTTCAGACAATTCAAGTGATCAAGATTTTAAAATATGAA AAGAAACTGGCCAAAATGTGCTTTTTAATGATATTCACCTTCCTGGTCTG TTGGATGCCTTATATCGTGATCTGCTTCTTGGTGGTTAATGGTCATGGTC ACCTGGTCACTCCAACAATATCTATTGTTTCGTACCTCTTTGCTAAATCG AACACTGTATACAATCCAGTGATTTATGTCTTCATGATCAGAAAGTTTCG AAGATCCCTTTTGCAGCTTCTGTGCCTCCGACTGCTGAGGTGCCAGAGGC CTGCTAAAGACCTACCAGCAGCTGGAAGTGAAATGCAGATCAGACCCATT GTGATGTCACAGAAAGATGGGGACAGGCCAAAGAAAAAAGTGACTTTCAA CTCTTCTTCCATCATTTTTATCATCACCAGTGATGAATCACTGTCAGTTG ACGACAGCGACAAAACCAATGGGTCCAAAGTTGATGTAATCCAAGTTCGT CCTTTGTAG"
dna_string = dna_string.replace('\n', '')
dna_string = dna_string.replace(' ', '')
results = []
start = 0

while start < len(dna_string) - 20 + 1:
    result = find_gc_sequence(dna_string[start:])
    if result:
        results.append(result)
        start += dna_string[start:].index(result) + 1
        if not (result.startswith('GC') or (result.endswith('GC') )):
            results.pop()
        # try:
        #     if any(result[i] == result[i+1] == result[i+2] == result[i+3] for i in range(len(result) - 3)):
        #         results.pop()
        # except:
        #     continue
    else:
        break
if results:
    i=0
    invalid_start_ends = ["GCC","GCG","GGC","CGG","CCG","CGC"]
    for seq in results:
        if ("TTTT" in seq or "AAAA" in seq or "CCCC" in seq or "GGGG" in seq):
            results.pop(i)
        elif (seq[-3:] in invalid_start_ends or seq[:3] in invalid_start_ends):
            results.pop(i)
        else:
            if seq.startswith('GC'):
                print(f"{i}. Found sequence: (R) {seq}")
            elif seq.endswith('GC'):
                print(f"{i}. Found sequence: (F) {seq}")
            i+=1
