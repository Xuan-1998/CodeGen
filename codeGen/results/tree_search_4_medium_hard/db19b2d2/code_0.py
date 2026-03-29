import math

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [0] * (n + 1)
    if s[h-1] > 0:
        dp[0] = 1
    else:
        dp[0] = 0

    for i in range(1, n+1):
        total_players_from_interest = sum(s[j] for j in range(h, i+1))
        if i >= h:
            dp[i] = (total_players_from_interest - 1) * (1 - 1/(i+1)) + dp[h-1]
        else:
            dp[i] = 0

    total_teams = math.comb(n, n)
    prob_at_least_one = sum(dp[i] for i in range(n))
    if total_teams == 0:
        print(-1)
    else:
        print(prob_at_least_one / total_teams)

if __name__ == "__main__":
    solve()
