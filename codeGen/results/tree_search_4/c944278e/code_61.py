import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    dp = [[[] for _ in range(2**n)] for _ in range(n+1)]
    dp[0][0] = [""]
    
    for i in range(n):
        for j in range(len(dp[i])):
            for k in range(2):
                team = "1" if s[n-1-i] == "1" else "0"
                new_teams = [t + team for t in dp[i][j]]
                if k:
                    new_teams.sort()
                dp[i+1][k].extend(new_teams)
    
    winning_teams = set()
    for i in range(2**n):
        for team in dp[n][i]:
            winning_teams.add(team)
    
    print("\n".join(sorted(list(winning_teams))))

if __name__ == "__main__":
    solve()
