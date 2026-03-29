import math

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Initialize dp array
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        gcd = math.gcd(arr[j], arr[i - 1])
        if gcd > 1 and gcd not in bad_primes:
            dp[i] = max(dp[i], dp[j - 1] + (i - j) * gcd)
    dp[i] = max(dp[i], sum(arr[:i]))

# Print the maximum beauty
print(max(dp))
