n, m = map(int, input().split())  
arr = list(map(int, input().split()))  
bad_primes = list(map(int, input().split()))

min_primes = []
for num in arr:
    min_divisor = num
    for bad_prime in bad_primes:
        if num % bad_prime == 0 and bad_prime < min_divisor:
            min_divisor = bad_prime
    min_primes.append(min_divisor)

beauties = []
for num in arr:
    if all(i > 1 for i in range(2, int(num ** 0.5) + 1)) or min_primes[arr.index(num)] not in bad_primes:
        beauties.append(num)
    else:
        beauties.append(int(num ** 0.5))

print(max(beauties))
