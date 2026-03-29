def countOnes(n):
    dp = [0] * (n + 1)
    for k in range(1, n + 1):
        for i in range(10):
            if i == 1:  # Count the number of ones in each position
                dp[k] += k // 10 ** (k.bit_length() - 1) * 9 + min(k % 2 ** (k.bit_length() - 1), 9)
    return sum(dp)

import sys

n = int(sys.stdin.readline())

print(countOnes(n))
