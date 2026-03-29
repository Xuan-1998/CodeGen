import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[0] * (max(arr) + 1) for _ in range(n)]

    for i in range(n):
        for j in range(max(arr) + 1):
            if arr[i] > j:
                dp[i][j] = 1
            else:
                dp[i][j] = max(dp[k][x] for k in range(i) if x < j)

    return max(max(row) for row in dp)

if __name__ == "__main__":
    input_arr = [int(x) for x in sys.stdin.readline().split()]
    print(longest_increasing_subsequence(input_arr))
