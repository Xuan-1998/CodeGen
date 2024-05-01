from collections import defaultdict

def find_winning_teams(n, s):
    dp = defaultdict(list)
    winning_teams = []

    for i in range(n):
        for j in range(2**i):
            k = (j >> (i - 1)) & 1
            if s[i-1] == '0' and k == 1:
                # Team j can win from this phase onwards
                dp[(i, j, k)].append((i, j, k))

    for ((i, j, k), _) in dp.items():
        # Check all possible winning conditions for team j with skill level k in phase i
        if any(s[p-1] == '0' and (k >> p) & 1 for p in range(i+1)):
            # Team j can win from this phase onwards, add it to the list
            winning_teams.append((i, j, k))

    winning_teams.sort(key=lambda x: sum(1 << i for i in range(n) if x[0] == i and (x[1] >> i) & 1))

    return [f"({i}, {j})" for (i, j, _) in winning_teams]
