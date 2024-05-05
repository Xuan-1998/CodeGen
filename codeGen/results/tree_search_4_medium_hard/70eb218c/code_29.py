import sys

def min_operations(n, x):
    dp = [float('inf')] * (10 ** (n - 1) + 1)
    dp[0] = 0

    for i in range(1, 10 ** (n - 1) + 1):
        if len(str(i)) == n:
            dp[i] = 0
        else:
            for d in str(i):
                if int(d) != 0:  # only update the state if the digit is not zero
                    dp[i] = min(dp[i], dp[int(d)] + 1)

    return -1 if dp[x] == float('inf') else dp[x]

n, x = map(int, input().split())
print(min_operations(n, x))
