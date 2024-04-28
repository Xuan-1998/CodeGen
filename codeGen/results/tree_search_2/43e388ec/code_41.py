import sys
input = lambda: int(input())

def solve():
    n = input()
    m = input()

    memo = {}
    dp = [[0]*(32) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(32):
            if i == 1:
                dp[i][j] = (m & (1 << j)) ^ ((m >> j) << 31)
            else:
                a = m & ((1 << j) - 1)
                b = m >> j
                dp[i][j] = dp[i-1][0]
                for k in range(32):
                    if k == j: continue
                    dp[i][j] ^= (a & (1 << k)) ^ ((b >> k) << 31)
            memo[(i, j)] = dp[i][j]

    res = sum(memo.values()) % (10**9 + 7)
    print(res)

if __name__ == "__main__":
    solve()
