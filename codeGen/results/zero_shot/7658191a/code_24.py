import sys

def max_score(arr, k, z):
    n = len(arr)
    dp = [0] * (k + 1)  # dynamic programming array
    for i in range(1, k + 1):
        if i <= z:
            # try to make as many rightward moves as possible
            dp[i] = max(dp[i - 1], arr[i] + dp[i - 1])
        else:
            # no more than z leftward moves allowed, so just add the value at index i
            dp[i] = arr[i]
    return dp[k]

t = int(sys.stdin.readline())
for _ in range(t):
    n, k, z = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(max_score(arr, k, z))
