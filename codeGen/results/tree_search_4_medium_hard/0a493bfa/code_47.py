import math

# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n  # Initialize dynamic programming state

def is_good_prime(p):
    for bad_p in b:
        if bad_p == p:
            return False
    return True

for i in range(1, n):
    pivot = a[i]
    new_a = a[:i] + a[i+1:]
    for j in range(len(new_a)):
        gcd = math.gcd(pivot, new_a[j])
        if is_good_prime(gcd):
            dp[i] = max(dp[i], f(dp[i-1]) + pivot)
        else:
            dp[i] = min(dp[i], f(dp[i-1]) - pivot)

print(dp[-1])

