from functools import lru_cache

def winning_teams(n, s):
    @lru_cache(None)
    def dfs(i, team_mask):
        if i == n:
            return [team_mask]
        
        result = []
        for j in range(1 << (n - i)):
            new_team_mask = team_mask | j
            if (s[i] == '0' and (j & 1)) or (s[i] == '1' and not (j & 1)):
                result.extend(dfs(i + 1, new_team_mask))
        return result
    
    return sorted({team_mask: bit_pattern(team_mask) for team_mask in dfs(0, 0)})

def bit_pattern(team_mask):
    pattern = ''
    for i in range(len(bin(team_mask)[2:])):
        if (team_mask >> i) & 1:
            pattern += 'W'
        else:
            pattern += 'L'
    return pattern

# Example usage
n = int(input())
s = input()
print(*winning_teams(n, s), sep='\n')
