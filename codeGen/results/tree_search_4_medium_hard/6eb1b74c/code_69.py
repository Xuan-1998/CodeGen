from collections import defaultdict

def solve(t, n, s):
    dp = defaultdict(int)
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(t) or j == n:
            return 0
        min_steps = float('inf')
        for k in range(n):
            if t[i:i+len(s[k])] == s[k]:
                new_j = j + 1
                steps = dfs(i+len(s[k]), new_j)
                min_steps = min(min_steps, 1 + steps)
        memo[(i, j)] = min_steps
        return min_steps

    min_steps = dfs(0, 0)
    if min_steps == float('inf'):
        return -1
    print(min_steps)

    used_strings = []
    i = len(t) - 1
    for _ in range(min_steps):
        j = n - 1
        while j >= 0:
            if (i, j) not in memo:
                break
            min_j = j
            min_i = i
            for k in range(n):
                if t[i:i+len(s[k])] == s[k]:
                    new_i = i+len(s[k])
                    new_j = j - 1
                    if (new_i, new_j) in memo:
                        min_i = new_i
                        min_j = new_j
            used_strings.append((min_j+1, min_i))
            i = min_i
            j = min_j
    for pair in used_strings[::-1]:
        print(*pair)

solve(input(), int(input()), [input() for _ in range(int(input()))])
