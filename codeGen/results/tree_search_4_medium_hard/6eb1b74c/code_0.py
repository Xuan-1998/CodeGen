import sys

def solve():
    t = input()
    n = int(input())
    s = [input() for _ in range(n)]

    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]
    last_used = [[0] * (n + 1) for _ in range(len(t) + 1)]

    for i in range(len(t) + 1):
        if i == 0:
            dp[i][n] = 0
        else:
            for j in range(n + 1):
                if j == 0 or i <= len(t):
                    if all(s[k] not in t[:i] for k in range(j)):
                        dp[i][j] = -1
                    else:
                        min_steps = float('inf')
                        last_used_index = j
                        for k in range(min(len(s), j), -1, -1):
                            if s[k] in t[:i]:
                                steps = dp[i - len(s[k])][k]
                                if steps != -1 and (steps + 1 < min_steps or (steps + 1 == min_steps and last_used_index > k)):
                                    min_steps = steps + 1
                                    last_used_index = k
                        dp[i][j] = min_steps

    if dp[-1][-1] == -1:
        print(-1)
    else:
        m = dp[-1][-1]
        for i in range(m):
            index = []
            pos = t.find(s[last_used[-1][i + 1]][last_used_index])
            while pos != -1:
                index.append((pos, last_used_index))
                pos = t.find(s[last_used_index], pos + len(s[last_used_index]))
            if not index:
                break
        print(m)
        for i in range(m):
            print(*index[i])

if __name__ == "__main__":
    solve()
