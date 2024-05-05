import sys

def beauty_contest(t, l, r):
    MOD = 10**9 + 7
    dp = [[0] * (r - l + 1) for _ in range(r - l + 1)]

    for i in range(2, r - l + 1):
        for k in range(l, i + l):
            if k == l:
                dp[i][k] = 0
            else:
                dp[i][k] = min(dp[j-1][k-1] + 2 * (i-j+1) for j in range(k-1, i))
            if k > l and k < r:
                dp[i][k] += dp[i-1][k-1]

    res = sum(i**t * dp[i][l+i-1] for i in range(1, r - l + 2)) - l * dp[r-l][r]
    return int(res % MOD)

if __name__ == "__main__":
    t, l, r = map(int, input().split())
    print(beauty_contest(t, l, r))
