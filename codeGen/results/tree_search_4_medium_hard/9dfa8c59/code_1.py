from collections import defaultdict

def solve(n_max, k_perms):
    # Step 1: Find all prime numbers up to n_max
    primes = set()
    for num in range(2, n_max + 1):
        if all(num % i for i in range(2, int(num ** 0.5) + 1)):
            primes.add(num)

    # Step 2: Count the permutations of each prime number that are also prime numbers
    dp = defaultdict(int)
    for num in primes:
        for p in range(len(str(num)), -1, -1):
            perms = int(''.join(sorted(map(str, (int(d) for d in str(num)))[:p])))
            if perms < n_max and perms in primes:
                dp[num] += 1

    # Step 3: Find the count of prime numbers with k_perms permutations, the smallest and largest such prime numbers
    count = sum(1 for k in dp.values() if k == k_perms)
    min_prime = max_prime = None
    for num, k in dp.items():
        if k == k_perms:
            min_prime = min(num, min_prime) if min_prime is None else min_prime
            max_prime = max(num, max_prime)

    return [count, min_prime or 0, max_prime or 0]

# Read input from stdin and print the output to stdout
n_max, k_perms = map(int, input().split())
print(solve(n_max, k_perms))
