import sys

def solve(t, s):
    n = len(s)
    m = len(t)

    dp = [[-1] * (n+1) for _ in range(m)]

    for i in range(m):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = 0
            else:
                last_string_used = -1
                for k in range(i):
                    if t[k:i].endswith(s[j]):
                        if dp[k-1][last_string_used] + 1 < dp[i][j]:
                            dp[i][j] = dp[k-1][last_string_used] + 1
                        last_string_used = j

    m_steps = -1
    for i in range(m):
        if dp[i][-1] != -1:
            m_steps = min(m_steps, dp[i][-1])
            break

    if m_steps == -1:
        return -1
    else:
        steps = []
        for i in range(m-1, -1, -1):
            last_string_used = -1
            for j in range(n+1):
                if t[i].endswith(s[j]):
                    if dp[i][j] == m_steps - 1:
                        steps.append((m_steps - 1, i))
                        last_string_used = j
            m_steps -= 1

        return str(m_steps) + '\n' + '\n'.join([' '.join(map(str, step)) for step in steps])

input()
t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]

print(solve(t, s))
