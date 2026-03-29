def solve(n_max, k_perms):
    count = 0
    min_prime = float('inf')
    max_prime = float('-inf')

    for i in range(2, n_max):  # iterate from 2 to n_max
        perms = prime_permutations(i)
        if len(perms) == k_perms:  # found a prime number with k_perms permutations
            count += 1
            min_prime = min(min_prime, min(perms))
            max_prime = max(max_prime, max(perms))

    return [count, min_prime, max_prime]

# Example usage:
n_max = int(input())
k_perms = int(input())

print(solve(n_max, k_perms))  # output: [count, smallest prime, largest prime]
