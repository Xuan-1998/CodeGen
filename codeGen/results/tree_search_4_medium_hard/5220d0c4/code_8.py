def max_beauty():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    dp = {}
    for i in range(n+1):
        for j in range(m+1):
            if (i, j) not in dp:
                if j == 0:
                    num_good_primes = sum(1 for x in arr[:i] if is_prime(x) and x not in bad_primes)
                    num_total_primes = i
                    dp[(i, j)] = max(num_good_primes, num_total_primes)
                else:
                    min_prime_divisor = float('inf')
                    for k in range(i):
                        prime_divisor = get_min_prime_divisor(arr[k])
                        if prime_divisor not in bad_primes and prime_divisor < min_prime_divisor:
                            min_prime_divisor = prime_divisor
                    num_good_primes = dp.get((k, j-1), 0) + (arr[i-1] % min_prime_divisor == 0)
                    num_total_primes = i
                    dp[(i, j)] = max(num_good_primes, num_total_primes)

    return dp[(n, m)]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_min_prime_divisor(n):
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            return i
