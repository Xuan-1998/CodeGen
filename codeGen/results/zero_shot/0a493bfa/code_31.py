import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

good_primes = set()
for p in range(2, 1000001):  # adjust the upper bound as needed
    if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1)):
        good_primes.add(p)

def is_good_prime(p):
    return p not in bad_primes and p in good_primes

def beauty(s):
    if s == 1:
        return 0
    min_prime = None
    for p in range(2, int(s ** 0.5) + 1):
        if s % p == 0 and is_good_prime(p):
            min_prime = p
            break
    if min_prime is None:
        return beauty(s - 1)
    elif is_good_prime(min_prime):
        return beauty(s // min_prime) + s
    else:
        return beauty(s // min_prime) - s

def max_beauty(arr):
    arr = list(arr)
    while True:
        new_arr = []
        for i in range(len(arr)):
            gcd_sum = 0
            for j in range(i + 1, len(arr)):
                gcd_sum += abs(gcd(arr[i], arr[j]))
            if gcd_sum > 0:
                new_arr.append(max_beauty([gcd(arr[i], x) for x in arr[i + 1:]]))
            else:
                new_arr.append(arr[i])
        if new_arr == arr:
            break
        arr = new_arr
    return sum(beauty(x) for x in arr)

print(max_beauty(arr))
