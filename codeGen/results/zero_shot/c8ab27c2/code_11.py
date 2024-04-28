s = input().strip()
t = input().strip()

def shortest_uncommon_subsequence():
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subseq = s[i:j]
            if not is_subsequence(subseq, t):
                return len(subseq)

    return -1

def is_subsequence(subseq, seq):
    i = j = 0
    while i < len(subseq) and j < len(seq):
        if subseq[i] == seq[j]:
            i += 1
        j += 1
    return i == len(subseq)

print(shortest_uncommon_subsequence())
