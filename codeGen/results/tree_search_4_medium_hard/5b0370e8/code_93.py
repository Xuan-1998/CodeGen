def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(2**k):
            and_count = 0
            xor_count = 0
            for j in range(k, -1, -1):
                if (i >> j) & 1:
                    and_count += 1
                    xor_count ^= 2**j - 1
                else:
                    and_count -= 1
                    xor_count ^= 2**j - 1
            for i in range(n + 1):
                for j in range(k, -1, -1):
                    if (i >> j) & 1:
                        dp[i][j] += and_count
                        dp[i][j] %= 10**9 + 7
                    else:
                        dp[i][j] -= and_count
                        dp[i][j] %= 10**9 + 7
        print((dp[n][k]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
