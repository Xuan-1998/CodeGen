import sys

def winning_teams(n, s):
    dp = [[0] * (1 << n) for _ in range(2**n)]
    teams = ['' + str(i) for i in range(2**n)]

    def dfs(i, score):
        if i >= len(s):
            return [team for team in teams if bin(score)[2:].zfill(n).count('1') == sum(int(c) for c in s)]

        res = []
        for j in range(len(dp[scores])):
            dp[scores][j] = 0
            for k in range(len(teams)):
                if (score >> i) & 1:
                    teams[k] += str(i)
                    dp[scores].append(k)
                else:
                    dp[scores].append(k)
            res.extend(dfs(i + 1, sum(int(c) for c in s)))
        return res

    scores = [0]
    for i in range(len(s)):
        if s[i] == '1':
            scores.append(sum(int(c) for c in s[:i + 1]))
    return dfs(0, 0)

n = int(input())
s = input()
print(*winning_teams(n, s), sep='\n')
