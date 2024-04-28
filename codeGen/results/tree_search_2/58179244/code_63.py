from collections import deque

def min_recolor(n, s):
    dp = [[0] * 3 for _ in range(2)]
    prev_color = {'R': 'G', 'G': 'B', 'B': 'R'}
    curr_color = ['R', 'G', 'B']

    for i in range(1, n + 1):
        for j in range(3):
            if s[i - 1] == curr_color[j]:
                dp[i % 2][j] = min(dp[(i - 1) % 2] + (1 if prev_color[curr_color[j]] != s[i - 2] else 0), dp[i % 2][k] for k in range(3) if k != j)
            else:
                dp[i % 2][j] = min(dp[(i - 1) % 2], dp[i % 2][k] for k in range(3) if k != j)

    r = min(dp[-1])
    res = []

    i, j = n, 0
    while i > 0:
        if s[i - 1] == curr_color[j]:
            res.append(curr_color[j])
            i -= 1
        else:
            j = (j + 1) % 3
            r -= 1

    return str(r) + '\n' + ''.join(res[::-1])

n = int(input())
s = input()
print(min_recolor(n, s))
