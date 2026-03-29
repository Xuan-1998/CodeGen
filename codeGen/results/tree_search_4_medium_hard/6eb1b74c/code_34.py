import sys

def solve(t, S):
    n = len(S)
    m = len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if t[i-1] == S[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

    min_steps = sys.maxsize
    for j in range(n, -1, -1):
        if t.count(S[j-1]) > 0:
            min_steps = j
            break

    if min_steps == sys.maxsize:
        return str(-1)
    else:
        steps = dp[m][n]
        result = []
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if t[i-1] == S[j-1]:
                    steps -= 1
                    if steps > 0:
                        result.append((j, i))
                    else:
                        break

        return str(steps) + '\n' + '\n'.join(map(str, result))

t = input().strip()
n = int(input())
S = [input().strip() for _ in range(n)]

print(solve(t, S))
