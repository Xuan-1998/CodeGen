import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1):
            if j == 0:
                dp[i][j] = 1
            else:
                max_length = 0
                for k in range(i-1):
                    if arr[k] < arr[j-1] and dp[k][j-1] + 1 > max_length:
                        max_length = dp[k][j-1] + 1
                dp[i][j] = max_length

    return max(max_row for row in dp)

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(arr))
