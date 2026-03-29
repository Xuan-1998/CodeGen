def solve():
    t = int(input())
    MOD = 10**9 + 7
    dp = [[0] * 2 for _ in range(30)]

    dp[0][0] = 1

    for k in range(1, 30):
        for j in (0, 1):
            if j == 0:
                dp[k][j] = dp[k-1][1]
            else:
                dp[k][j] = (dp[k-1][0] + dp[k-1][1]) % MOD

    ans = [0] * t
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = 2**k - 1
        xor_result = sum(1 << i for i in range(k)) if any(i < k for i in range(n)) else 0
        ans[_] = (dp[k][and_result >= xor_result]) % MOD

    return '\n'.join(map(str, ans))

print(solve())
