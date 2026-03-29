inf = float("inf")

def tabulate_small_n(n):
    dp = [[inf] * (10 ** (n - 1) + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for x in range(1, 10 ** (i - 1) + 1):
            if len(str(x)) == i:
                dp[i][x] = 0
            else:
                min_ops = inf
                for d in str(x):
                    for y in "0123456789":
                        new_x = int(str(x).replace(d, str(int(d) * int(y))), 10)
                        if len(str(new_x)) == i - 1:
                            min_ops = min(min_ops, dp[i - 1][new_x] + 1)
                dp[i][x] = min_ops
    return dp

def recursive_memoization(n, x):
    if len(str(x)) == n:
        return 0
    dp = [[inf] * (10 ** (n - 1) + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for y in str(x):
            new_x = int(str(x).replace(y, "0" * len(str(x)) + y), 10)
            if len(str(new_x)) == i - 1:
                dp[i][x] = min(dp[i][x], recursive_memoization(i - 1, new_x) + 1)
    return dp[n][x]

def solve(n, x):
    if n <= 5:
        return tabulate_small_n(n)[n][x]
    else:
        return recursive_memoization(n, x)

while True:
    n, x = map(int, input().split())
    print(solve(n, x))
