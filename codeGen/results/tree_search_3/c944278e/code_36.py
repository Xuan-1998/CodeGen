from math import factorial

def get_winning_teams(n, s):
    # Initialize a dictionary to store the winning teams for each state
    memo = {}

    def dfs(i, j, seen, path):
        # If all phases have been processed, return the current team's skill level as the winning team
        if i == n:
            return [(seen | 1 << i, (j - sum((bit & 1) for bit in s)))]

        # Check if we've already computed this state
        if (i, j) in memo:
            return memo[(i, j)]

        # Initialize the result list and the current winning teams set
        res = []
        seen_teams = set()

        # Iterate over each possible team's skill level for the current phase
        for k in range(j + 1):
            # Check if the current team's skill level is greater than or equal to its opponents' average skill level
            if k >= sum((bit & 1) for bit in s[:i]) / i:
                # Recursively generate all winning teams for this subproblem and add them to the result list
                res.extend(dfs(i + 1, k, seen | (1 << i), path + [k]))

        # Store the computed state in the memo dictionary
        memo[(i, j)] = res

        return res

    # Generate all winning teams for the entire tournament
    return [team for _, team in sorted(set(sum((bit & 1) for bit in s)) * (factorial(2 ** n),), key=lambda x: sum((bit & 1) for bit in x[0])))

# Read the input from standard input
n = int(input())
s = list(map(int, input()))

print(get_winning_teams(n, s))
