def find_winning_teams(n, s):
    dp = [[[] for _ in range(2**n)] for _ in range(n + 1)]

    def dfs(i, s):
        if i == n:
            return [s]
        if dp[i][int(s, 2)]:
            return dp[i][int(s, 2)]
        
        winning_teams = []
        for j in range(2**n):
            team_result = (s >> (n - i - 1)) & 1
            if (team_result == 0) != (j & (1 << (n - i - 1))):
                # Team wins or loses, add the winning teams to our set
                new_winning_teams = dfs(i + 1, bin(j)[2:].zfill(n))
                if team_result:
                    winning_teams.extend(new_winning_teams)
        
        dp[i][int(s, 2)] = winning_teams
        return winning_teams

    return dfs(0, s)

# Example usage
n = int(input())
s = input()
winning_teams = find_winning_teams(n, s)
print(*sorted(winning_teams), sep='\n')
