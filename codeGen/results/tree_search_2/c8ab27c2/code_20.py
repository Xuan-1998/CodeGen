def shortest_uncommon_subsequence(S, T):
    memo = {}

    def helper(k, p):
        if (k, p) in memo:
            return memo[(k, p)]
        
        uncommon_length = -1
        for i in range(p, len(S) - k + 1):
            subseq = S[i:i+k]
            if not is_subsequence(subseq, T):
                uncommon_length = k
                break
        
        memo[(k, p)] = uncommon_length
        return uncommon_length

    def is_subsequence(subseq, seq):
        i, j = 0, 0
        while i < len(subseq) and j < len(seq):
            if subseq[i] == seq[j]:
                i += 1
            j += 1
        return i == len(subseq)

    k = 1
    while True:
        uncommon_length = helper(k, 0)
        if uncommon_length != -1:
            break
        k += 1
    
    return uncommon_length

def get_input():
    S = input().strip()
    T = input().strip()
    return S, T

S, T = get_input()
print(shortest_uncommon_subsequence(S, T))
