def minUncommonLength(S, T):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(S) or j == len(T):
            return float('inf')
        if S[i] != T[j]:
            return 1 + min(dp(i+1, j), dp(i, j+1))
        return dp(i+1, j+1)
    return dp(0, 0)

S = input().strip()
T = input().strip()

print(minUncommonLength(S, T))

