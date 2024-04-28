def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    dp = [{} for _ in range(n + 1)]
    res = float('inf')

    for i in range(1, n + 1):
        if S[i - 1] not in T:
            for j in range(i):
                k = i - j
                if all(S[j:j+k] != T[:k]):
                    dp[k][S[j:j+k]] = k
                    res = min(res, k)

    return res if res != float('inf') else -1

# Example usage:
S = input()
T = input()
print(shortest_uncommon_subsequence(S, T))
