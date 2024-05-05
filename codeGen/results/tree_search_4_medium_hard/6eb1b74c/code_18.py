from collections import defaultdict

def min_steps_to_color(text, strings):
    n = len(strings)
    dp = [[-1] * (len(text) + 1) for _ in range(len(text) + 1)]
    used_strings = [0] * n
    memo = [[False] * (len(text) + 1) for _ in range(len(text) + 1)]

    def dfs(i, j):
        if memo[i][j]:
            return dp[i][j]
        if i == 0:
            if j >= len(text):
                return 0
            else:
                return -1
        used = False
        for k in range(n):
            if strings[k] in text[:j + 1]:
                idx = text.index(strings[k], i)
                if idx < j and not used:
                    used = True
                    dp[i][j] = min(dp[i][j], dfs(i, idx - 1) + 1) if used_strings[k] else -1
                if idx == j or not used:
                    used_strings[k] += 1
        if not used:
            dp[i][j] = dfs(i - 1, j)
        memo[i][j] = True
        return dp[i][j]

    m = dfs(len(text), len(text))
    counts = defaultdict(int)
    for i in range(m):
        for j in range(i + 1):
            if used_strings[0]:
                print(f"{i} {j}")
            else:
                break

    print(m)

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        text = input()
        n = int(input())
        strings = [input() for _ in range(n)]
        min_steps_to_color(text, strings)
