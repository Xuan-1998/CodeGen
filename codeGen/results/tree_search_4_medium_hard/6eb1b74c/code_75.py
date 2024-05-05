def solve(text, strings):
    dp = {}

    def helper(i, n):
        if (i, n) in dp:
            return dp[(i, n)]

        if i >= len(text) or n == 0:
            return 0

        steps = float('inf')
        for j, s in enumerate(strings):
            if text[i:].startswith(s):
                steps = min(steps, helper(i + len(s), n - 1))
                break

        dp[(i, n)] = steps + (steps == 0)
        return dp[(i, n)]

    res = []
    m = helper(0, len(strings))

    if m == float('inf'):
        print(-1)
    else:
        i = 0
        for _ in range(m):
            found = False
            for j, s in enumerate(strings):
                if text[i:].startswith(s):
                    res.append((j, i))
                    found = True
                    break
            i += len(s)

    print(m)
    for w, p in res:
        print(f"{w} {p}")
