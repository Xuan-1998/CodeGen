def find_winning_teams(n):
    dp = [set() for _ in range(1 << n)]
    dp[0] = {0}

    for i in range(1, 1 << n):
        for j in range(i):
            if (i & j) == 0:
                continue
            dp[i].update(dp[j])

    winning_teams = []
    for i in range(1 << n):
        if len(dp[i]) > 0:
            winning_teams.append(dp[i])

    return sorted([f"Team {i+1}" for i, _ in enumerate(winning_teams)])

n = int(input())
print(*find_winning_teams(n), sep='\n')
