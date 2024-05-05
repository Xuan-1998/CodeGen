def count_prime_permutations(n_max, k_perms):
    dp = [[0] * (k_perms + 1) for _ in range(n_max + 1)]
    prime_count = 0
    smallest_prime = largest_prime = None

    for i in range(2, n_max + 1):
        if is_prime(i):  # Check if the number is prime
            perms = count_permutations(i)
            for k in range(min(k_perms, perms), -1, -1):  # Iterate over the table in reverse order
                dp[i][k] += 1  # Update the counter
                if dp[i][k] == k:  # If we've found the required count of prime numbers with exactly k permutations
                    if smallest_prime is None or i < smallest_prime:
                        smallest_prime = i
                    if largest_prime is None or i > largest_prime:
                        largest_prime = i
                    break

    return [prime_count, smallest_prime, largest_prime]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    perms = set()
    while n > 0:
        digit = n % 10
        n //= 10
        perms.add(int(''.join(map(str, [digit] + list(map(int, str(n)))))))
    return len(perms)

if __name__ == "__main__":
    n_max, k_perms = map(int, input().split())
    print(*count_prime_permutations(n_max, k_perms), sep='\n')
