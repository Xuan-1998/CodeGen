def main():
    n_max, k_perms = map(int, input().split())
    primes = generate_primes(n_max)
    result = filter_primes(primes, k_perms)
    print(*result)

if __name__ == '__main__':
    main()
