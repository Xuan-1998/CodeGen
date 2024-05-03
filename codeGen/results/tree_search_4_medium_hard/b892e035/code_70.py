import sys

# Read input from stdin
T = int(input())
for _ in range(T):
    n = int(input())
    memo = {}

    def dp(i, count1, count2):
        if (i, count1, count2) in memo:
            return memo[(i, count1, count2)]
        
        if i == 0:
            return 1

        p1 = (count1 / i) * (count2 / (i - 1)) * P[i]
        p2 = sum(dp(i - 1, count1 - 1, j) for j in range(A[i], B[i] + 1)) / (B[i] - A[i] + 1)
        
        memo[(i, count1, count2)] = max(p1, p2)
        return memo[(i, count1, count2)]

    P = [0] * (n + 1)
    for i in range(n):
        P[i], _, _ = map(float, input().split())

    result = dp(n, n, 0)
    print("{:.6f}".format(result))
