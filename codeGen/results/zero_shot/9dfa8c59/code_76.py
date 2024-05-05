n_max = int(input())
k_perms = int(input())

primes = sieve_of_eratosthenes(n_max)

counts = [count_prime_perms(p) for p in primes]

smallest = None
largest = None
count = 0
for i, (prime, count) in enumerate(zip(primes, counts)):
    if count == k_perms:
        if smallest is None or prime < smallest:
            smallest = prime
        if largest is None or prime > largest:
            largest = prime
        count += 1

print([count, smallest, largest])
