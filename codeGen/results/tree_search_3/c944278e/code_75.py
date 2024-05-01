def find_winning_teams():
    n = int(input())  # Read the number of phases from standard input
    s = input()  # Read the binary string representing the tournament results

    winning_teams = set()
    memo = {}

    def dfs(state):
        if state in memo:
            return memo[state]
        result = []
        for i in range(n - 1, -1, -1):
            if (state >> i) & 1:  # If the team wins in this phase
                new_state = state ^ (1 << i)
                result.append(i + 1)
                winning_teams.update(result)
            else:
                break
        memo[state] = tuple(sorted(result))
        return memo[state]

    for i in range(2 ** n):
        dfs(i)

    print(*sorted(winning_teams), sep='\n')

find_winning_teams()
