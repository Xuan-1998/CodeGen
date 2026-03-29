code_block
def color_text(t, s):
    n = len(s)
    dp = [[[float('inf')] * n for _ in range(n)] for _ in range(len(t) + 1)]
    memo = [[[None] * n for _ in range(n)] for _ in range(len(t) + 1)]

    count = 0
    for i in range(1, len(t) + 1):
        for j in range(1, n + 1):
            for k in range(j):
                if memo[i][j][k] is not None:
                    continue
                min_steps = float('inf')
                for w in range(k, j):
                    if t[i-1:i+len(s[w])-1].startswith(s[w]):
                        min_steps = min(min_steps, dp[i-len(s[w])][w-1][k] + 1)
                memo[i][j][k] = min_steps
        count += 1

    if any(dp[-1][i][0] > len(t) for i in range(n)):
        return -1
    else:
        return count, [str((i+1, p)) for i, p in enumerate(memo[-1][0])]

while True:
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]
    res = color_text(t, s)
    if res == -1:
        print(res)
    else:
        print(*res[0])
        for r in res[1]:
            print(r)
