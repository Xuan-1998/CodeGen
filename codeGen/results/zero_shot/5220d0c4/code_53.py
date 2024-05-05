def find_max_bauty(n, m, arr, bad_primes):
    max_beauty = 0
    for i in range(1 << n):  # generate all subsets of arr
        subset_sum = sum([arr[j-1] if ((i & (1 << j))) else 0 for j in range(1, n+1)])
        prime_divisors = [p for p in bad_primes if subset_sum % p == 0]
        min_prime_divisor = min(prime_divisors) if prime_divisors else 0
        beauty = -min_prime_divisor if min_prime_divisor in bad_primes else min_prime_divisor
        max_beauty = max(max_beauty, beauty)
    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))
print(find_max_bauty(n, m, arr, bad_primes))
