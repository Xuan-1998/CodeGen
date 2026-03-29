import sys

def color_text(t, S):
    n = len(S)
    dp = [[float('inf')] * (n + 1) for _ in range(len(t) + 1)]
    memo = {}

    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:
            return 0
        if j == 0:
            return float('inf')

        min_steps = float('inf')
        for k in range(j - 1, -1, -1):
            common = 0
            for x in range(min(i, len(S[k])), -1, -1):
                if t[i - x - 1] == S[k][x]:
                    common += 1
                else:
                    break

            min_steps = min(min_steps, f(i - common, k) + (i > common))
        dp[i][j] = min_steps
        memo[(i, j)] = min_steps
        return min_steps

    m = len(t)
    for i in range(1, m + 1):
        j = n - 1
        while j >= 0:
            if dp[i][j] != float('inf'):
                break
            j -= 1

    steps = f(m, n - 1)

    if steps == float('inf'):
        print(-1)
    else:
        for i in range(1, m + 1):
            k = n - 1
            while k >= 0 and dp[i][k] != steps:
                k -= 1
            print(f"{k + 1} {i - len(S[k]) - 1}")
