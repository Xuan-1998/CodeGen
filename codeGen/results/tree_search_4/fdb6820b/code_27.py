def solve():
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in arr:
            if i >= num:
                dp[i] += dp[i - num]

    print(dp[N] % (10**9 + 7))

if __name__ == "__main__":
    solve()
