import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)

max_beauty = 0

for num in a:
    # Check if the number is prime and not in the set of bad primes
    is_good_prime = True
    for bad_prime in b:
        if num % bad_prime == 0:
            is_good_prime = False
            break
    
    if is_good_prime:
        # Apply the operation to reduce the number
        while num > 1 and any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
            p = next(i for i in range(2, int(num ** 0.5) + 1) if num % i == 0)
            num //= p
        
        # Recalculate the beauty of the reduced number
        # TO DO: Implement the logic to calculate the beauty of a reduced number
        beauty = ...
        
        max_beauty = max(max_beauty, beauty)

print(max_beauty)
