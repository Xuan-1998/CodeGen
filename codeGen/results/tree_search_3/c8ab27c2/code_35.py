def shortest_uncommon_subsequence():
    S, T = input().split(), input().split()
    dp = {(i, j): 0 for i in range(len(S)+1) for j in range(len(T)+1)}
    
    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            if S[i-1] == T[j-1]:
                dp[(i, j)] = dp[(i-1, j-1)] + 1
            else:
                dp[(i, j)] = max(dp[(i-1, j)], dp[(i, j-1)]) + 1
    
    return len(S) - dp[(len(S), 0)] if dp[(len(S), 0)] != len(T) else -1

print(shortest_uncommon_subsequence())
