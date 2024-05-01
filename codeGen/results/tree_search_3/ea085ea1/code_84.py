from collections import defaultdict

def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Precompute all possible substrings for each string
    substrings = defaultdict(set)
    for i in range(N):
        for j in range(i, N):
            substring = str1[i:j+1]
            substrings[substring].add((i, j))

    def dfs(i, j):
        if i == N or j == N:
            return 0
        if dp[i][j]:
            return dp[i][j]

        # Check if the current characters match and update dp[i][j] accordingly
        if str1[i] == str2[j]:
            dp[i][j] = 1 + dfs(i - 1, j - 1)
        else:
            dp[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))

        return dp[i][j]

    # Initialize the maximum number of common non-overlapping substrings
    max_count = 0

    for i in range(N):
        for j in range(i, N):
            substring = str1[i:j+1]
            if substring in substrings and dfs(i, j) > max_count:
                max_count = dfs(i, j)

    return max_count

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(max_common_substrings(str1, str2))
