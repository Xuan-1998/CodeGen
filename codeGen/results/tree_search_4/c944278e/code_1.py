from collections import defaultdict

def find_winning_teams(n, s):
    dp = defaultdict(bool)
    dp[0] = [i+1 for i in range(n) if s[i] == '1']
    
    for i in range(1, n):
        new_winners = set()
        for j in range(len(dp[i-1])):
            winner_id = dp[i-1][j]
            if int(s[i]) == 1:
                new_winners.add(winner_id)
            else:
                for k in range(n):
                    if s[k] == '1' and k not in dp[i-1]:
                        new_winners.add(k+1)
        dp[i] = list(new_winners)

    return sorted(dp[n-1])

n = int(input())
s = input().strip()
print(find_winning_teams(n, s))
