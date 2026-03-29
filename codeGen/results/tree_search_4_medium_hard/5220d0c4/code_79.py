import sys

# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Initialize table with 0s
table = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0:
            # Base case: beauty value is 0 when the subarray is empty
            table[i][j] = 0
        elif j > 0:
            last_elem = arr[i - 1]
            min_prime_divisor = next((p for p in range(2, int(last_elem ** 0.5) + 1) if last_elem % p == 0), None)
            is_good_prime = min_prime_divisor not in bad_primes

            # State transition
            table[i][j] = max(table[i - 1][j], table[i - 1][max(0, j - 1)])
            if is_good_prime:
                table[i][j] += (last_elem % 2 == 0)
            else:
                table[i][j] -= (last_elem in bad_primes)

print(table[-1][-1])  # Output the maximum beauty value
