s = input().strip()
t = input().strip()

def shortest_uncommon_subsequence(s, t):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subseq = s[i:j]
            if not is_subsequence(subseq, t) and all(not subseq in x for x in [t[:i], t[i+1:]]):
                return len(subseq)
    return -1

def is_subsequence(sub, seq):
    i = j = 0
    while i < len(sub) and j < len(seq):
        if sub[i] == seq[j]:
            i += 1
        j += 1
    return i == len(sub)

print(shortest_uncommon_subsequence(s, t))
