def count_ways(A, N):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(i):
            if j < len(A) and j + A[j] <= i:
                dp[i] += dp[j]

    return dp[N] % (10**9 + 7)

m, N = map(int, input().split())
A = list(map(int, input().split()))
print(count_ways(A, N))
