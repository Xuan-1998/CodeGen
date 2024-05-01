from collections import deque

def find_winning_teams(n, s):
    memo = {}
    winning_teams = []

    def dp(phase, remaining_teams):
        if (phase, tuple(sorted(remaining_teams))) in memo:
            return memo[(phase, tuple(sorted(remaining_teams)))]
        
        if phase == n:
            return [list(remaining_teams)]
        
        result = []
        for i, team in enumerate(remaining_teams):
            next_teams = remaining_teams[:i] + remaining_teams[i+1:]
            if s[phase-1] & (1 << i):  # Team wins
                result.extend(dp(phase+1, next_teams | {team}))
            else:  # Team loses
                result.extend(dp(phase+1, tuple(sorted(set(next_teams) - {team}))))
        
        memo[(phase, tuple(sorted(remaining_teams)))] = result
        return result

    dp(0, set())
    
    for teams in sorted([list(team) for team in dp(n, set())], key=lambda x: sum(x)):
        winning_teams.append((teams, sum(teams)))

    return [team[1] for team in sorted(winning_teams)]

# Example usage:
n = int(input())  # Input: the number of phases
s = input()  # Input: the binary string representing the tournament results

result = find_winning_teams(n, s)
print(*result, sep='\n')
