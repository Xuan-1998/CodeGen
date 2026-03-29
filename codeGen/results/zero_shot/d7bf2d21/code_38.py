import sys

def find_lis_count(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    max_length = 0
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + 1) for k in range(j+1, i)]
                max_length = max(max_length, dp[i][j])

    return max_length

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(find_lis_count(arr))
