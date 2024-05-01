def winning_teams(n):
    memo = {}
    for mask in range(1 << n):
        teams = [i for i in range(n) if (mask >> i) & 1]
        if len(teams) == 1:
            # Base case: only one team remains
            memo[mask] = [teams[0]]
        else:
            # Recursive case: divide the tournament into smaller phases
            left, right = teams[:len(teams)//2], teams[len(teams)//2:]
            left_winning_teams = winning_teams(len(left))
            right_winning_teams = winning_teams(len(right))
            for team in left_winning_teams:
                memo[mask] = list(set(memo[mask] + [team]))
            for team in right_winning_teams:
                memo[mask] = list(set(memo[mask] + [team]))

    return [sorted(list(teams)) for teams in memo.values()]

n = int(input())
print(*winning_teams(n), sep='\n')
