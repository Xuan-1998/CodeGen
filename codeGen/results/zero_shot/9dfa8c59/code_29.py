def count_prime_permutations(n_max, k_perms):
    # Step 1: Generate all prime numbers below n_max
    primes = []
    for num in range(2, n_max):
        if is_prime(num):
            primes.append(num)

    # Step 2: Count the number of prime numbers with k_perms prime permutations
    count = 0
    for prime in primes:
        # Check if the number of prime permutations is equal to k_perms
        if has_k_perms(prime, k_perms):
            count += 1

    # Step 3: Find the smallest and largest prime numbers among those with k_perms prime permutations
    smallest = None
    largest = None
    for prime in primes:
        if has_k_perms(prime, k_perms):
            if smallest is None or prime < smallest:
                smallest = prime
            if largest is None or prime > largest:
                largest = prime

    return [count, smallest, largest]

def is_prime(num):
    # Check if a number is prime using the Sieve of Eratosthenes algorithm
    sieve = [True] * (num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, num + 1, i):
                sieve[j] = False
    return sieve[num]

def has_k_perms(prime, k_perms):
    # Check if a prime number has exactly k_perms prime permutations
    perms = set()
    for digit in str(prime):
        for p in perms:
            yield from int(str(p) + digit)
        perms.add(digit)
    return len(perms) == k_perms

n_max, k_perms = map(int, input().split())
print(count_prime_permutations(n_max, k_perms))
