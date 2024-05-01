from collections import defaultdict

def findWinningTeams(n, s):
    memo = defaultdict(list)
    for i in range(1 << n):  # Iterate over all prefixes of the input binary string
        winners = [] if s[i - 1] == '0' else [i - 1]
        for j in range(i):
            if s[j] == '0':
                winners.extend([k for k, v in memo[(j, s[:j])].items() if not v])
            else:
                winners.append(i - 1)
        memo[i, s] = winners
    winning_teams = set()
    for i in range((1 << n) - 1, -1, -1):  # Iterate over the dp table in reverse order
        if len(memo[i, s]) > 0:
            winning_teams.update(memo[i, s])
    return sorted(list(winning_teams))

n = int(input())
s = input()
print(findWinningTeams(n, s))
