import math
dp = [[-1]*200002 for _ in range(1000001)]
def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        res = solve_dp(n, m)
        print(res % (10**9+7))

def solve_dp(n, m):
    if dp[n][m] != -1:
        return dp[n][m]
    if m == 0:
        dp[n][m] = n
    else:
        prev_length = 9
        for i in range(1, n):
            new_length = math.ceil(math.log10(prev_length + 1))
            dp[i][m] = min(dp[i][m], 1 + solve_dp(new_length, m-1))
    return dp[n][m]

solve()
