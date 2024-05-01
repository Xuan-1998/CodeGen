===BEGIN CODE===
def uncommon_subsequence_length(S, T):
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(S) or j == len(T):
            return max(len(S) - i, len(T) - j)

        if S[i] != T[j]:
            return 1 + min(dfs(i + 1, j), dfs(i, j + 1))

        memo[(i, j)] = 1 + dfs(i + 1, j + 1)
        return memo[(i, j)]

    result = float('inf')
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] != T[j]:
                result = min(result, len(S) - i - dfs(i + 1, j))
                break

    return result if result != float('inf') else -1
