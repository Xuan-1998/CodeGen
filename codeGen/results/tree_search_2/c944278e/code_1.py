from itertools import combinations

def winning_teams(n):
    # Initialize the table with 2^N possible teams
    dp = [[[] for _ in range(2**n)] for _ in range(2**n)]

    # Base case: when n = 0, there are no teams and therefore no winning teams
    if n == 0:
        return []

    # Fill up the table using bottom-up dynamic programming
    for i in range(1 << n):
        for j in range(i + 1, (1 << (n+1))):
            dp[j][i] = [team for team in combinations(range(n), n) if team[i % n]]

    # Find all the winning teams by iterating over the table
    winning_teams = []
    for i in range(2**n):
        for j in range(i + 1, (1 << (n+1))):
            if len(dp[j][i]) > 0:
                winning_teams.extend(sorted(list(set([team for team in dp[j][i]]))))

    return sorted(list(set(winning_teams)))

# Test the function
n = int(input())
print(winning_teams(n))
