from collections import deque

def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, min(i+1, N)+1):
            if str1[:i] == str2[:j]:
                dp[i][j] = max(dp[i-1][k-1] + 1 for k in range(j+1))
            else:
                dp[i][j] = 0

    return max(max(row) for row in dp)

print(find_common_substrings())
