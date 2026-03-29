import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_min_prime_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return None

def calculate_beaniness(array):
    beauty = 0
    for num in array:
        min_prime = find_min_prime_divisor(num)
        if is_prime(min_prime):
            beauty += 1
        else:
            beauty -= 1
    return beauty

n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = -10**9
for i in range(1 << n):  # all possible subsets of the array
    subset_array = [num for j, num in enumerate(array) if (i >> j) & 1]
    beauty = calculate_beaniness(subset_array)
    if beauty > max_beauty:
        max_beauty = beauty

print(max_beauty)
