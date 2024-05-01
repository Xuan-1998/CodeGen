from functools import lru_cache

def shortest_uncommon_subsequence(S, T):
    @lru_cache(None)
    def dp(i, j):
        if i == 0 or j == 0:
            return max(i, j)

        if S[i-1] == T[j-1]:
            return dp(i-1, j-1) + 1
        else:
            return min(dp(i-1, j), dp(i, j-1))

    m, n = len(S), len(T)
    uncommon_length = -1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] != T[j-1]:
                uncommon_length = max(uncommon_length, dp(i, j))
    
    return uncommon_length

if __name__ == "__main__":
    S, T = input().split()
    print(shortest_uncommon_subsequence(S, T))
