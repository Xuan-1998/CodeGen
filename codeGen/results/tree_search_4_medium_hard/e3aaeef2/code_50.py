def solve():
    t = int(input())
    MOD = 10**9 + 7

    dp = [[1] * (m+1) for _ in range(11)]

    for i in range(1, 11):
        for j in range(1, m+1):
            if i < 10:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = min(dp[i//10][j-1], (i%10) + 1)

    for _ in range(t):
        n, m = map(int, input().split())
        print((dp[get_digit_count(n)][m]) % MOD)

def get_digit_count(n):
    return len(str(n))
