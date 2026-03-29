def sieve_of_eratosthenes(n_max):
    sieve = [True] * (n_max + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False
    return [i for i in range(2, n_max + 1) if sieve[i]]

def prime_permutations(n):
    digits = len(str(n))
    perms = set()
    for p in itertools.permutations(str(n)):
        perm = int(''.join(map(str, p)))
        if is_prime(perm):
            perms.add(perm)
    return len(perms)

def main():
    n_max, k_perms = map(int, input().split())
    primes = sieve_of_eratosthenes(n_max)
    count = 0
    smallest = largest = 0
    for prime in primes:
        if prime_permutations(prime) == k_perms:
            count += 1
            if not smallest:
                smallest = prime
            largest = prime
    print(count, smallest, largest)

if __name__ == "__main__":
    main()
