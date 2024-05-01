from collections import defaultdict

def winning_teams(n, s):
    # Initialize memo dictionary
    memo = defaultdict(list)

    def dp(i, teams):
        if i == n:
            return [teams]
        if (i, tuple(sorted(teams))) in memo:
            return memo[(i, tuple(sorted(teams))))]
        
        win_team = []
        for team in range(2**n):
            if bin(team ^ int('1' + '0'*i, 2)).count('1') == s[i]:
                new_teams = teams | (1 << team)
                winning_teams = dp(i+1, new_teams)
                if not win_team or len(winning_teams) > len(win_team):
                    win_team = winning_teams
        memo[(i, tuple(sorted(teams)))] = win_team
        return win_team

    # Call the function
    result = dp(0, 0)

    # Print the results
    for team in set(map(lambda x: format(x, 'b').zfill(n).count('1'), result)):
        print(team)

# Receive input from stdin and print the answer to stdout
n = int(input())
s = input()
winning_teams(n, s)
