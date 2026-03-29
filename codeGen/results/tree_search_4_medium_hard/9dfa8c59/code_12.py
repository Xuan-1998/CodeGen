from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations_count(num):
    count = 1
    digits = [int(d) for d in str(num)]
    for p in permutations(digits):
        permuted_num = int("".join(map(str, p)))
        if is_prime(permuted_num):
            count += 1
    return count

def solve():
    n_max, k_perms = map(int, input().split())
    primes = []
    for i in range(2, n_max + 1):
        if is_prime(i):
            primes.append(i)
    
    dp = [0] * (n_max + 1)
    dp[2] = 1
    
    for prime in primes:
        count = 0
        for num in range(prime, n_max + 1):
            if is_prime(num) and prime_permutations_count(num) == k_perms:
                count += 1
        dp[prime] = count
    
    smallest = max_i = 0
    for i, count in enumerate(dp):
        if count > 0 and (smallest == 0 or i < smallest):
            smallest = i
        if count > 0 and i > max_i:
            max_i = i
    
    return [sum(1 for count in dp if count >= k_perms), smallest, max_i]

print(solve())
