import sys

def count_subarrays(Arr, K):
    N = len(Arr)
    dp = [0] * (N + 1)  # initialize dp array with zeros
    dp[0] = 0  # base case: no subarrays at index 0

    for i in range(N):
        max_val = max(Arr[:i+1])  # find maximum element up to index i
        if max_val > K:
            dp[i+1] = dp[i] + 1  # increment dp if max_val > K
        else:
            dp[i+1] = dp[i]  # keep dp as previous value

    return dp[-1]  # return the final value of dp, which represents the answer

# Read input from stdin
N, K = map(int, sys.stdin.readline().split())
Arr = list(map(int, sys.stdin.readline().split()))

print(count_subarrays(Arr, K))
