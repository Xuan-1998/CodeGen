import sys

def find_longest_increasing_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[1] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[j - 1] > arr[j - 2]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

    return sum(1 for row in dp[-1] if max(row) == len(arr))

print(find_longest_increasing_subsequences())
