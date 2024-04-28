s = input().strip()
t = input().strip()

def uncommon_subsequence(s, t):
    subseq_len = float('inf')
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if substr not in t:
                subseq_len = min(subseq_len, j - i)
            else:
                break
    return -1 if subseq_len == float('inf') else subseq_len

print(uncommon_subsequence(s, t))
