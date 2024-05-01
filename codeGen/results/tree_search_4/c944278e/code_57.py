def can_win(i, team_idx):
    if i == n:  # base case: check if team wins at least once
        return wins[team_idx] == '1'
    if memo.get((i, team_idx)):
        return memo[(i, team_idx)]
    
    # recursive step: update wins string based on current phase result
    if s[i]:
        next_wins = wins[:team_idx] + ('1' if wins[team_idx] != '0' else '0') + wins[team_idx+1:]
    else:
        next_wins = wins
    
    # store result for memoization
    result = can_win(i+1, team_idx)
    
    memo[(i, team_idx)] = result  # store the result
    
    return result

n = int(input())  # read input n
s = input()  # read binary string s of length n
wins = '0' * (2**n)  # initialize wins string
memo = {}  # memoization dictionary

winning_teams = [i for i in range(2**n) if can_win(0, i)]
print(*winning_teams, sep='\n')  # print winning teams
