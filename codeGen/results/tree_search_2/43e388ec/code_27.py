import sys

def solve(a, b):
    MOD = 10**9 + 7
    memo = [[0] * (10**5 + 1) for _ in range(21)]

    def dp(x, i):
        if x == 0:
            return 0
        res = memo[x][i]
        if res != 0:
            return res
        res = dp((x & b), min(i, len(bin(b)) - 2))
        res = (res + ((a ^ (x << 1)) % MOD)) % MOD
        memo[x][i] = res
        return res

    ans = 0
    for i in range(314160):
        ans = (ans + dp(a, i)) % MOD
    return ans

# Read input from stdin and print the answer to stdout
a, b = map(int, input().split())
print(solve(a, b))
