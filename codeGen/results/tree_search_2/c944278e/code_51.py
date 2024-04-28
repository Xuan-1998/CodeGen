import sys

def winning_teams(n):
    dp = [[False] * (1 << n) for _ in range(2**n)]
    skill_levels = [0] * (1 << n)

    for i in range(1 << n):
        if i & 1:  # The team has won
            dp[i][i ^ 1] = True
            skill_levels[i] += 1
        else:
            dp[i][i ^ 1] = False
            skill_levels[i] -= 1

    winning_teams = []
    for i in range(2**n):
        if all(dp[i][j] for j in range(1 << n) if j & i):
            winning_teams.append(bin(i)[2:].zfill(n))

    return sorted(winning_teams)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(*winning_teams(n), sep='\n')
