from collections import defaultdict

def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    memo = defaultdict(int)
    dp = [[-1 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

    def dfs(i, j):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if S[i] == T[j]:
            dp[i][j] = 1 + dfs(i-1, j-1)
        else:
            dp[i][j] = max(dfs(i-1, j), dfs(i, j-1))
        return dp[i][j]

    shortest_uncommon_subsequence_length = float('inf')
    for i in range(len(S)):
        for j in range(len(T)):
            length = dfs(i, j)
            if length < shortest_uncommon_subsequence_length:
                shortest_uncommon_subsequence_length = length

    print(shortest_uncommon_subsequence_length)

find_shortest_uncommon_subsequence()
