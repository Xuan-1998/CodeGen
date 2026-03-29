import sys

def read_input():
    return [int(x) for x in input().split()]

def solve(dp, arr):
    n = len(arr)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == "__main__":
    arr = read_input()
    n = len(arr)
    dp = [0] * (n + 1)
    print(solve(dp, arr))
