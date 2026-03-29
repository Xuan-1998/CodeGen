import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n+1) for _ in range(n+1)]
    prev_sign = None
    for i in range(1, n+1):
        if signs[i-1] == '+':
            sign = 1
        else:
            sign = -1

        if prev_sign is not None and sign != prev_sign:
            dp[i][i] = min(dp[i-1][i-1], 0)
        elif sign == prev_sign:
            l, r = i-1, i-1
            while l >= 0 and signs[l] == sign:
                l -= 1
            while r < n and signs[r] == sign:
                r += 1
            dp[i][i] = min(dp[i-1][i-1], (r-l+1)//2)
        else:
            l, r = i-1, i-1
            while l >= 0 and signs[l] != sign:
                l -= 1
            while r < n and signs[r] != sign:
                r += 1
            dp[i][i] = min(dp[i-1][i-1], (r-l+1)//2)

        prev_sign = sign

    for _ in range(q):
        l, r = map(int, input().split())
        print(min([dp[l][j] + dp[j+1][r] - dp[l][r] for j in range(l, r+1)]))

if __name__ == "__main__":
    solve()
