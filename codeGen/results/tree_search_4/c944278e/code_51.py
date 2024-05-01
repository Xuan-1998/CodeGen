import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    dp = {0: set()}
    for i in range(1, n+1):
        if s[i-1] == '1':
            dp[i] = dp[i-1].copy()
            dp[i].add(i)
        else:
            dp[i] = dp[i-1].copy()

    winning_teams = set()
    for team in range(2**n):
        won_at_least_once = False
        for phase in range(n):
            if (team >> phase) & 1 and s[phase] == '1':
                won_at_least_once = True
                break
        if won_at_least_once:
            winning_teams.add(team)

    print(' '.join(map(str, sorted(winning_teams))))

if __name__ == '__main__':
    solve()
