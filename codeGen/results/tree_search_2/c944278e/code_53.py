from collections import deque

def winning_teams(n, s):
    # Initialize a memoization dictionary
    dp = {}

    def dfs(i, t):
        if (i, t) in dp:
            return dp[(i, t)]

        # Base case: only one team can win when n = 1
        if i == 0:
            return [(0, int(t[0]))]

        # Calculate the skill levels of each team and compare them
        teams = []
        for j in range(2 ** i):
            teams.append((j, int(t[j]))

        # Sort the teams based on their skill levels
        teams.sort(key=lambda x: x[1])

        # Initialize a queue to store the winning teams
        queue = deque()

        # Add the first team as it's the winner in this case
        for team in teams:
            if len(queue) == 0:
                queue.append(team)
            else:
                last_team = queue[-1]
                if team[1] > last_team[1]:
                    queue.append(team)

        # Return the winning teams
        return [(i, t) for i, t in enumerate(queue)]

    # Main function to calculate and print the winning teams
    result = []
    for i in range(n - 1, -1, -1):
        if (i, s[:2 ** i]) not in dp:
            result.extend(dfs(i, s[:2 ** i]))
        else:
            result.extend(dp[(i, s[:2 ** i])])

    # Print the winning teams
    for team in result:
        print(team[0], team[1])
