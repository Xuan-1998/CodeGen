S = input()
T = input()

def uncommon_subsequence_length(S, T):
    S_len = len(S)
    T_len = len(T)

    for i in range(1 << (min(S_len, T_len))):
        temp_S = S
        temp_T = T
        
        for j in range(min(S_len, T_len)):
            if ((i & (1 << j)) > 0):
                temp_S = temp_S[:j] + temp_S[j+1:]
                temp_T = temp_T[:j] + temp_T[j+1:]
            else:
                break

        if set(temp_S) != set(temp_T):
            return len(S) - len(temp_S)

    return -1

print(uncommon_subsequence_length(S, T))
