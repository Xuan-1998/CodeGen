def winning_teams(n):
    memo = {}

    def dp(i, s):
        if i < 0:
            return [0]
        if (i, s) not in memo:
            teams = []
            for j in range(2**n):
                opponents = dp(i-1, bin(j)[2:].zfill(n))
                if all(opponent != j for opponent in opponents):
                    teams.append(j)
            memo[(i, s)] = teams
        return memo[(i, s)]

    winning_teams = []
    for s in map(lambda x: bin(x)[2:].zfill(n), range(2**n)):
        teams = dp(n-1, s)
        if teams:
            winning_teams.append(int(s, 2))
    return sorted(winning_teams)

if __name__ == "__main__":
    n = int(input())
    print(*winning_teams(n), sep="\n")
