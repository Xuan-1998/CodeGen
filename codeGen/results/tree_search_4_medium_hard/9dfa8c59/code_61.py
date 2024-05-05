from itertools import permutations

def prime_permutations(n_max, k_perms):
    # Initialize the results dictionary
    results = {i: [0, i, i] for i in range(1, n_max + 1)}

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_permutations(n):
        p = str(n)
        perms = set(permutations(p))
        return len([p for p in perms if ''.join(p) != p and is_prime(int(''.join(p)))])

    def dp(n, k_perms):
        if n <= 1:
            return [0, 0, 0]

        if results[n][0] > 0:
            return results[n]

        count = 0
        for i in range(2, n + 1):
            if is_prime(i) and count_permutations(i) == k_perms:
                count += 1

        if count > 0:
            min_prime = max_prime = int(''.join(map(str, sorted(set(str(i) for i in range(2, n + 1) if is_prime(i))))))

        results[n] = [count, min_prime, max_prime]
        return results[n]

    # Main function
    count, min_prime, max_prime = dp(n_max, k_perms)
    return [count, min_prime, max_prime]


# Read input from standard input
n_max, k_perms = map(int, input().split())

# Print the result to standard output
print(*prime_permutations(n_max, k_perms))
