def findWinningTeams(n):
    dp = {}
    
    def dfs(s):
        if s not in dp:
            wins = sum(1 for i in range(n) if (s >> i) & 1)
            if wins >= 2 ** (n - 1):
                return [str(i + 1) for i in range(n) if (s >> i) & 1]
            result = []
            for i in range(n):
                new_s = s ^ (1 << i)
                if new_s not in dp:
                    dp[new_s] = dfs(new_s)
                result.extend(dps[s][i])
            return result
    
    def solve():
        teams = list(range(2 ** n))
        result = []
        for team in teams:
            s = 0
            for i in range(n):
                if (team >> i) & 1:
                    s ^= 1 << i
            result.extend(dfs(s))
        return set(tuple(sorted(map(int, team.split())))) | set(result)
    
    print('\n'.join(str(team) for team in sorted(list(solve()))))
