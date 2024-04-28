def solve(a, b):
    MOD = 10**9 + 7
    dp = {}
    result = 0

    for i in range(314161):  # include 0 and 314159
        if (i, a, b) not in dp:
            dp[(i, a, b)] = ((a ^ (b << 1)) % MOD + result) % MOD
        result = dp[(i, a, b)]

    return result

# Read input from stdin
a, b = map(int, input().split())
print(solve(a, b))
