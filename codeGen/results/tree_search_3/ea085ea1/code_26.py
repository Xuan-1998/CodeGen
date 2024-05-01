from collections import defaultdict

def solve(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                continue

            common_substrs = defaultdict(int)
            for k in range(1, min(i, j) + 1):
                substr = str1[i - k:i]
                if substr in str2[:j]:
                    common_substrs[substr] += 1

            dp[i][j] = max(common_substrs.values(), default=0)

    return dp[N][N]

str1 = input()
str2 = input()

print(solve(str1, str2))
