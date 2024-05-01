===BEGIN CODE===
def find_max_common_substrings():
    N = int(input())
    str1, str2 = input().strip(), input().strip()

    dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            if i > 0 and j > 0:
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    visited[i][j] = True

    max_common_substrings = 0
    for i in range(N+1):
        for j in range(N+1):
            if visited[i][j]:
                max_common_substrings = max(max_common_substrings, dp[i][j])

    print(max_common_substrings)

find_max_common_substrings()
===END CODE===
