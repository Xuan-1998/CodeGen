import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def beauty(arr, bad_primes):
    max_beauty = 0
    for _ in range(len(arr)):
        new_arr = [arr[0]]
        for i in range(1, len(arr)):
            gcd_val = gcd(new_arr[-1], arr[i])
            if gcd_val != arr[i]:
                new_arr.append(gcd_val)
        beauty = 0
        for num in new_arr:
            p = next((p for p in bad_primes if is_prime(p) and p <= num), None)
            if p:
                beauty -= num
            else:
                beauty += num
        max_beauty = max(max_beauty, beauty)
    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

print(beauty(arr, bad_primes))
