n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

def min_prime_divisor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

arr_beauty = [min_prime_divisor(x) for x in arr]

def is_bad_prime(n):
    return n in bad_primes

arr_beauty = [min_prime_divisor(x) if is_bad_prime(x) else -min_prime_divisor(x) for x in arr]
max_beauty = max(arr_beauty)
print(max_beauty)
