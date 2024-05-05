def find_max_beauty(n, m, arr, bad_primes):
    max_beauty = 0

    for num in arr:
        min_prime_divisor = 2
        while num % min_prime_divisor != 0 and min_prime_divisor <= int(num**0.5) + 1:
            min_prime_divisor += 1

        if min_prime_divisor in bad_primes:
            max_beauty -= min_prime_divisor
        else:
            max_beauty += min_prime_divisor

    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = find_max_beauty(n, m, arr, bad_primes)

print(max_beauty)
