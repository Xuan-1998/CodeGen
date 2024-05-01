import sys

def solve(n, s):
    # Initialize memoization table
    dp = [[[[] for _ in range(2)] for _ in range(2 ** i)] for i in range(n + 1)]

    def dfs(i, state):
        if i > n:
            return [[]]
        if dp[i][state][0]:
            return [[int(''.join(map(str, list(bin(state)[2:])), '0b'))]]

        result = []
        for j in range(2 ** (n - i)):
            if s[n - 1 - i] == bin(j ^ state)[2:].zfill(n - i).count('1') % 2:
                next_state = state ^ (1 << (n - 1 - i))
                result.extend([team] + dfs(i + 1, next_state) for team in [[int(''.join(map(str, list(bin(j)[2:])), '0b'))]] if not [team] in dp[i][state]):
        return result

    # Main function
    return dfs(0, 0)

# Read input from stdin
n = int(input())
s = input().strip()

# Print winning teams to stdout
print('\n'.join(map(str, solve(n, s))))
