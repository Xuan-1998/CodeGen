def main():
    n_max, k_perms = map(int, input().split())
    primes = sieve_of_eratosthenes(n_max)
    result = filter_prime_numbers(primes, k_perms)
    print(*result)

if __name__ == "__main__":
    main()
