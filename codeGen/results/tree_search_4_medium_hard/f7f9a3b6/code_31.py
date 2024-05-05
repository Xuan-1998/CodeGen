def solve():
    n, = map(int, input().split())
    s, = [input() for _ in range(n)]
    a, = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(27)]

    for i in range(26):
        for j in range(n, -1, -1):
            if j <= n and s[j-1].lower() == chr(i+97):
                dp[i][j] = dp[i][j-1]
            else:
                if a[i] > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-a[i]] + 1)
                else:
                    dp[i][j] = 1

    res = [0, 0, float('inf')]
    for j in range(n+1):
        if dp[25][j] > res[0]:
            res[0] = dp[25][j]
            res[2] = j
        if res[0] - res[0]%10**9 + 7 < n:
            res[0] -= (res[0]-1)%10**9 + 7

    print(res[0]%10**9 + 7)
    print(res[2])
    print(min(26, (n+res[0]-1)//10**9 + 7))

if __name__ == "__main__":
    solve()
