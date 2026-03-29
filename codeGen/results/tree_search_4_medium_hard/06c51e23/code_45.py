from collections import defaultdict

def max_grade(n, t, f):
    state = [[False] * (t + 1) for _ in range(n + 1)]
    memo = defaultdict(bool)

    def dfs(i, j):
        if state[i][j]:
            return memo[(i, j)]

        if i == 0:
            state[i][j] = True
            return True

        result = False
        for k in range(1, t + 1):
            if j - k >= 0 and dfs(i - 1, j - k):
                if int((10 ** k) * f) % 10 > 4 or (int((10 ** k) * f) % 10 == 5 and j < k + t):
                    result = True
                state[i][j] = result
                break

        memo[(i, j)] = result
        return result

    if dfs(n, t):
        return int(str(int(f * (10 ** n)))[2:])
    else:
        return -1
