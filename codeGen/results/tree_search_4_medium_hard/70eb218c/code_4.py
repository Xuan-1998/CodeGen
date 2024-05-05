from sys import stdin

def min_operations(n, x):
    memo = [[-1 for _ in range(20)] for _ in range(20)]

    def dp(i, k):
        if i == 2:
            return 0
        if k == 0:
            return -1
        if memo[i][k] != -1:
            return memo[i][k]
        if x % 10 == 0:
            res = min(dp(i-1, k-1), dp(i, k-1)) + 1
        else:
            res = dp(i, k-1) + 1
        memo[i][k] = res
        return res

    return dp(n, len(str(x)))

n, x = map(int, stdin.readline().split())
print(min_operations(n, x))
