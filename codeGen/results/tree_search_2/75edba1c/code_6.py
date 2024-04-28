import sys

def count_subarrays(K):
    N = int(sys.stdin.readline())
    Arr = [int(x) for x in sys.stdin.readline().split()]
    dp = [0] * N

    max_val = max(Arr)
    if max_val <= K:
        return 0

    dp[0] = 1 if Arr[0] > K else 0
    for i in range(1, N):
        dp[i] = 1 if max(Arr[:i+1]) > K and dp[i-1] == 0 else 0

    return sum(dp)

print(count_subarrays(int(sys.stdin.readline())))
