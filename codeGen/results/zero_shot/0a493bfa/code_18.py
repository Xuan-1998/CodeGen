import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(s, good_primes):
    if s == 1:
        return 0
    min_prime_divisor = next((p for p in range(2, int(math.sqrt(s)) + 1) if s % p == 0), None)
    if min_prime_divisor not in good_primes:
        return f(s // min_prime_divisor, good_primes) - s
    else:
        return f(s // min_prime_divisor, good_primes) + s

def maximize_beauty(n, m, a, b):
    max_beauty = 0
    for _ in range(100):  # Try different numbers of operations
        beauty = 0
        array = [a[i] for i in range(n)]
        while True:
            max_gcd = 1
            for i in range(n):
                for j in range(i + 1, n):
                    gcd_val = math.gcd(array[i], array[j])
                    if gcd_val > max_gcd:
                        max_gcd = gcd_val
            for i in range(n):
                array[i] = max_gcd
            beauty += f(sum(array), b)
            if beauty > max_beauty:
                max_beauty = beauty
            else:
                break
    return max_beauty

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(maximize_beauty(n, m, a, b))
