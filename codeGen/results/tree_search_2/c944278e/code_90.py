from sys import stdin

def can_win(skill_levels, memo):
    n = len(skill_levels)
    teams = [bool(i) for i in range(2**n)]
    
    def dp(phase, teams_left):
        if phase >= n or not teams_left:
            return 0
        if (phase, tuple(teams_left)) in memo:
            return memo[(phase, tuple(teams_left))]
        
        max_skill = 0
        for i in range(n):
            if skill_levels[i] > max_skill and teams_left[i]:
                max_skill = skill_levels[i]
                max_win = dp(phase + 1, [j ^ (1 << i) for j in teams_left])
                if max_win:
                    max_skill += dp(phase + 1, [j ^ (1 << i) for j in teams_left])
        
        memo[(phase, tuple(teams_left))] = max_skill
        return max_skill
    
    win_teams = []
    for i in range(n):
        if skill_levels[i] > 0 and can_win([skill_levels[j] for j in range(n)] + [0], {(i, tuple([j ^ (1 << i) for j in range(2**n)]))}) >= dp(i + 1, [j ^ (1 << i) for j in range(2**n)]):
            win_teams.append(i)
    
    print(*win_teams)
