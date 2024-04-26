def solve():
    seq = input().strip()
    for i in range(len(seq)):
        if len(seq) % (i + 1) == 0:
            pattern = seq[:i + 1]
            if seq[i:] == pattern * (len(seq) // (i + 1)):
                return "Circular"
    return "Not Circular"

print(solve())
