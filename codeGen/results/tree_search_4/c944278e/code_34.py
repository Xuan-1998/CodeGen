import sys

def get_winning_team(phase, team):
    # Assuming skill levels are represented as binary strings of length n
    skill_level = int(bin(int(str(team), 2))[2:].zfill(n), 2)
    return [team for team in range(2**n) if bin(int(str(team), 2))[2:].zfill(n) > str(skill_level)]

def solve(n, s):
    dp = [[False] * (1 << n) for _ in range(n + 1)]
    winning_teams = []

    for i in range(n):
        for j in range(1 << n):
            if s[i] == '1':
                dp[i + 1][j | (1 << i)] = get_winning_team(i, j)
            else:
                dp[i + 1][j & ~(1 << i)] = get_winning_team(i, j)

    for k in range(1 << n):
        if dp[n][k]:
            winning_teams.append(k)

    return sorted(winning_teams)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(*solve(n, s), sep='\n')
