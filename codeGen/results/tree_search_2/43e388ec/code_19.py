from collections import defaultdict

memo = defaultdict(int)

def dp(a, b, i):
    if a == 0 or b == 0:
        return 0
    key = (a & b, i)
    if memo[key]:
        return memo[key]
    res = ((a ^ (b << i)) % (10**9 + 7))
    memo[key] = res
    return res

a = int(input(), 2)
b = int(input(), 2)

for i in range(314159):
    dp(a, b, i)

print(sum(dp(a, b, i) for i in range(314159)) % (10**9 + 7))
