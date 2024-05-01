import sys

def read_input():
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    return n, seq

def solve(n, seq):
    dp = [[0] * 105 for _ in range(105)]
    predecessor = [False] * (n + 1)
    predecessor[0] = True
    for i in range(1, n + 1):
        if i > 1 and seq[i - 1] == seq[i - 2]:
            predecessor[i] = True
        dp[i][seq[i - 1]] += 1

    max_points = 0
    for k in range(1, 105):
        total_points = 0
        for i in range(n + 1):
            if i > 0 and (i == 1 or predecessor[i] or not dp[i][k]):
                total_points += dp[i - 1][k]
        max_points = max(max_points, total_points)
    return max_points

n, seq = read_input()
print(solve(n, seq))
