S = input()
T = input()

def uncommon_subsequence_length(S, T):
    S_len = len(S)
    T_len = len(T)

    for i in range(S_len - T_len + 1):
        subseq = S[i:i+T_len]
        if subseq not in T:
            return len(subseq)
    
    return -1

print(uncommon_subsequence_length(S, T))
