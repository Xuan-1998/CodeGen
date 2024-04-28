from collections import defaultdict

def shortest_uncommon_subsequence(S, T):
    dp = {(0, p): 1 for p in range(len(S))}

    for k in range(1, min(len(S), len(T)) + 1):
        for p in range(len(S) - k):
            if S[p:p+k] not in T:
                dp[(k, p)] = k
                break
        else:
            continue

        for j in range(p + 1, len(S)):
            if S[j:j+k] not in T and S[j-k:j] == S[p:p+k]:
                return k
    return -1
