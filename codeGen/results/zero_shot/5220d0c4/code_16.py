import sys

def beauty(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    min_prime = None
    for i in range(2, n + 1):
        if is_prime(i) and (min_prime is None or i < min_prime):
            min_prime = i

    beauty = 0
    if is_prime(n) and n not in bad_primes:
        beauty += 1
    if min_prime is not None and min_prime > 1:
        beauty -= 1

    return beauty

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

max_beauty = 0
for num in array:
    max_beauty = max(max_beauty, beauty(num))

print(max_beauty)
