from collections import defaultdict

def dfs(i, j):
    if dp[i][j] != -1:  # memoized value exists
        return dp[i][j]

    min_steps = float('inf')
    for si in strings:
        if t[i:i+len(si)].endswith(si):  # string si present in substring
            steps = dfs(i+len(si), j)
            if steps != -1:  # impossible to color all letters in this range
                return -1
            min_steps = min(min_steps, steps + 1)

    dp[i][j] = min_steps if min_steps != float('inf') else -1
    return dp[i][j]

def solve():
    global dp, strings

    n = int(input())  # number of strings
    strings = [input() for _ in range(n)]  # list of strings

    t = input()  # text to color
    m, j = len(t), -1  # minimum number of steps and last index colored

    dp = [[-1]*len(t) for _ in range(len(t))]

    for i in range(m):
        if dfs(0, m-1) == -1:  # impossible to color all letters
            print(-1)
            return

        j += len(strings[dfs(0, m-1)-1])  # update last index colored
        print(dfs(0, m-1), end='\n')
        for _ in range(dfs(0, m-1)):
            w = dfs(0, m-1)
            p = j - len(strings[w-1])
            print(w, p, end='\n')
            j -= len(strings[w-1])

    print()

solve()
