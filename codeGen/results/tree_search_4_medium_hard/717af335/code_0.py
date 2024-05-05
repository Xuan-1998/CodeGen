def solve(A, B):
    dp = [float('inf')] * (A + 1)
    dp[0] = 0

    for x in range(1, A + 1):
        y = A - x
        if ((x & y) ^ B) == 0 and (x + y) == A:
            dp[x] = min(dp[x], x)

    return -1 if dp[A] == float('inf') else dp[A]

A = int(input())
B = int(input())

print(solve(A, B))
