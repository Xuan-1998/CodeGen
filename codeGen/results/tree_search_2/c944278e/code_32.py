import sys

def count_winning_teams(n):
    # Initialize a dictionary to store the results of subproblems
    memo = {0: ['']}

    def dfs(score, path):
        if score not in memo:
            memo[score] = []
        for i in range(1 << n):  # iterate over all possible skill levels
            new_score = score ^ (i << (n - 1))
            if new_score >= len(memo):
                return [(path + str(i),)]
            result = [p for p in dfs(new_score, path + str(i)) if int(p[0], 2) > sum(int(x, 2) for x in memo[new_score])]
            memo[score].extend(result)
        return memo[score]

    winning_teams = set()
    for i in range(1 << n):  # iterate over all possible skill levels
        dfs(i, str(i))[0][0]  # get the first permutation of teams with this skill level
        if int(''.join(reversed(map(str, bin(i)[2:].zfill(n)))), 2) == i:
            winning_teams.add(''.join(reversed(map(str, bin(i)[2:].zfill(n)))))

    print('\n'.join(sorted(winning_teams)))
