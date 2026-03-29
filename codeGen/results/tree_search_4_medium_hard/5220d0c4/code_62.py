import sys
from collections import defaultdict

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

# Pre-compute all primes up to the maximum array element
primes = []
for i in range(2, max(arr)+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

# Initialize dp array
dp = [[0]*(m+1) for _ in range(n+1)]

# Fill dp array using dynamic programming
for i in range(1, n+1):
    for j in range(min(m+1, len([p for p in primes if p <= arr[i-1]])), 0, -1):
        if arr[i-1] not in bad_primes:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        else:
            dp[i][j] = min(max(dp[i-1][j], 0), dp[i-1][j-1])

# Print maximum beauty of the array
print(max(dp[n]))
