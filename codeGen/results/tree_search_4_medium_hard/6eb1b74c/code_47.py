def solve(t, s):
    n = len(s)
    dp = [[float('inf')] * (n + 1) for _ in range(len(t) + 1)]

    dp[0][0] = 0

    for i in range(1, len(t) + 1):
        for j in range(min(i, n) + 1):
            if j == 0:
                continue
            for k in range(j):
                new_chars = t[i - len(s[k]):i].count(s[k])
                dp[i][j] = min(dp[i][j], dp[i - len(s[k])][k] + (new_chars > 0))

    if dp[-1][-1] == float('inf'):
        return -1
    else:
        steps, used_strings = [], []
        i, j = len(t), n
        while i > 0 and j > 0:
            for k in range(j):
                new_chars = t[i - len(s[k]):i].count(s[k])
                if new_chars > 0:
                    used_strings.append((k + 1))
                    steps.append((new_chars, i - len(s[k])))
                    i -= len(s[k])
                    j -= 1
                    break
        return min_steps

if __name__ == "__main__":
    t = input()
    n = int(input())
    s = [input() for _ in range(n)]
    print(solve(t, s))
