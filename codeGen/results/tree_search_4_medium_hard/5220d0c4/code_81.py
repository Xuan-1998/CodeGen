from math import sqrt

def min_prime_divisor(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = 0

for num in arr:
    min_divisor = min_prime_divisor(num)
    
    if min_divisor not in bad_primes:
        max_beauty += 1

print(max_beauty)
