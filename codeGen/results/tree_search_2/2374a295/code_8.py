def goodSequences(n, k):
    MOD = 1000000007

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = 1
            else:
                count = 0
                for x in range(j, i // MOD + 2):
                    if i % x == 0 and x >= j:
                        count += 1
                dp[i][j] = (dp[i][j - 1] * count) % MOD

    return sum(dp[n]) % MOD


def main():
    n, k = map(int, input().split())
    print(goodSequences(n, k))


if __name__ == "__main__":
    main()
