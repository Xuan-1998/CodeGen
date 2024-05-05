from collections import defaultdict

def solve(t, S):
    dp = [[float('inf')] * len(S) for _ in range(len(t)+1)]
    used_strs = [{} for _ in range(len(t)+1)]

    def match(s, j):
        if s in used_strs[i]:
            return used_strs[i][s]
        used_strs[i][s] = 0
        for k in range(len(s)):
            if t[i+k] != s[k]:
                break
        else:
            used_strs[i][s] = 1
            return 1
        return 0

    dp[0][0] = 0
    for i in range(1, len(t)+1):
        for j in range(len(S)):
            if match(S[j], i-1):
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
    res = []
    i, j = len(t), 0
    while i > 0 and j >= 0:
        if match(S[j], i-1):
            i -= len(S[j])
            res.append((len(S)-j-1, i))
            j -= 1
        else:
            j -= 1
    return dp[-1][-1], '\n'.join(map(lambda x: f'{x[0]} {x[1]}', res))

t = input()
n = int(input())
S = [input() for _ in range(n)]
min_steps, steps_trace = solve(t, S)
print(min_steps)
print(steps_trace)
