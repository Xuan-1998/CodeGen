import sys

def solve(n):
    dp = [[[] for _ in range(2)] for _ in range(n + 1)]
    memo = {}

    def dfs(i, s):
        if (i, s) in memo:
            return memo[(i, s)]

        if i == 0:
            return [int(s[0])]

        teams = []
        for j in range(2 ** (n - i)):
            bit = (j >> (n - i - 1)) & 1
            if bit == int(s[n - i - 1]):
                continue

            next_s = s[:n - i] + str(bit)
            teams.extend(dfs(i - 1, next_s))
        return sorted(list(set(teams)))

    for i in range(n + 1):
        dp[i][0] = []
        dp[i][1] = []

    for i in range(1, n + 1):
        for j in range(2 ** (n - i)):
            bit = (j >> (n - i - 1)) & 1
            if bit == 1:
                next_s = str(bit) + ''.join(map(str, bin(j)[3:][::-1]))
            else:
                next_s = '0' * (n - i) + str(bit)

            dp[i][bit] = sorted(list(set(dfs(i, next_s))))

    return '\n'.join(map(str, dp[n]))

input()
n = int(input())
print(solve(n))
