def main():
    n_max = int(input())
    k_perms = int(input())

    primes = sieve_of_eratosthenes(n_max)
    result = count_prime_permutations(primes, k_perms)

    print(*result, sep='\n')

if __name__ == '__main__':
    main()
