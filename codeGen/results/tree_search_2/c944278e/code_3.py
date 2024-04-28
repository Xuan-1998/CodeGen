def findWinningTeams(n, s):
    # Initialize the dynamic programming table
    dp = [[False] * (1 << n) for _ in range(1 << n)]

    # Base case: when there are no teams, any permutation is a winning team
    dp[0][0] = True

    # Fill up the dynamic programming table
    for mask1 in range(1 << n):
        for mask2 in range(1 << n):
            if dp[mask1][mask2]:
                for i in range(n):
                    new_mask1 = (mask1 ^ ((1 << i) - 1))
                    new_mask2 = (mask2 | (1 << i))
                    if s[i] == '1':
                        dp[new_mask1][new_mask2] = True
                    else:
                        dp[new_mask1][new_mask2] = False

    # Find all winning teams
    winning_teams = []
    for mask in range(1 << n):
        if dp[0][mask]:
            winning_teams.append(bin(mask)[2:].zfill(n))

    return sorted(winning_teams)

# Test the function
n = int(input())
s = input()
print(findWinningTeams(n, s))
