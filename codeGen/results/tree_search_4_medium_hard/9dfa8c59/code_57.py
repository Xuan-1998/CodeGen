import sys

# Read input from stdin
n_max, k_perms = map(int, input().split())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Initialize dp dictionary with [0, 0, 0] as default value
dp = {i: [0, 0, 0] for i in range(2, n_max+1)}

for i in range(2, n_max+1):
    if is_prime(i):
        # Count prime numbers with k_perms permutations below i
        count = sum(is_prime(j) and len(str(j)) == k_perms for j in range(2, i))
        dp[i][0] = count
        dp[i][1] = min(dp[i][1], i if is_prime(i) else 0)
        dp[i][2] = max(dp[i][2], i if is_prime(i) else 0)

# Print the result
print(*dp[n_max][0:3])
