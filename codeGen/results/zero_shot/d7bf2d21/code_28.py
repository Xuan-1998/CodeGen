import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * (max(arr) + 1) for _ in range(n)]

    for i in range(n):
        for j in range(1, max(arr) + 1):
            if arr[i] >= j:
                dp[i][j] = 1
            elif i > 0 and j > arr[i]:
                dp[i][j] = max(dp[k][j-1] for k in range(i)) + 1

    max_length = max(max(row) for row in dp)
    return sum(1 for row in dp if max(row) == max_length)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequences(arr))
