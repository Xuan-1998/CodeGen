import math

def f(s):
    if s == 1:
        return 0
    
    good_primes = set()
    for i in range(2, int(s ** 0.5) + 1):
        if is_prime(i) and i not in bad_primes:
            good_primes.add(i)
    
    p = min(good_primes & {i for i in range(2, s)} | {s})
    return f(s // p) + (1 if p in good_primes else -1) * s

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_initial_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        beauty += f(num)
    return beauty

def improve_array(arr):
    while True:
        new_arr = []
        for num in arr:
            gcd = 1
            for other_num in arr:
                if num != other_num and gcd == 1:
                    gcd = math.gcd(num, other_num)
            new_arr.append(gcd)
        if all(x == y for x, y in zip(arr, new_arr)):
            break
        arr = new_arr
    
    return arr

def calculate_final_beauty(arr):
    beauty = 0
    for num in arr:
        beauty += f(num)
    return beauty

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

initial_beauty = calculate_initial_beauty(arr, bad_primes)

print(initial_beauty)

new_arr = improve_array(arr)
final_beauty = calculate_final_beauty(new_arr)

print(final_beauty)
