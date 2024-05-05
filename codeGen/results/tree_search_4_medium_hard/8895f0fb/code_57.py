import sys
from collections import namedtuple

Test = namedtuple('Test', 'N')
T, N = [int(x) for x in input().split()]
for _ in range(T):
    A, B = [str(int(x)).zfill(N) for x in input().split()]
    n = len(A)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1):
            if int(A[-i]) > int(B[-j]):
                dp[i][j] += 9 - int(B[-j])
            elif int(A[-i]) < int(B[-j]):
                dp[i][j] += int(B[-j]) - 1
    expected_carries = sum(dp[i][i-1] for i in range(1, n+1)) / (n*(n+1)//2)
    print(f"{expected_carries:.6f}")
