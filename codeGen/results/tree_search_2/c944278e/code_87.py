from sys import stdin

def solve(n):
    dp = [0] * (1 << n)
    for s in range(1 << n):
        total_skill = 0
        winning_teams = []
        for i in range(n):
            if ((s >> i) & 1):  # team wins the match
                total_skill += 2 ** i
                winning_teams.append(i + 1)
            else:  # team loses the match, skip it
                continue
        if len(winning_teams) > 0:
            dp[s] = total_skill
    return [str(t) for t in sorted(set(winning_teams))]

n = int(stdin.readline())
print(*solve(n), sep='\n')
