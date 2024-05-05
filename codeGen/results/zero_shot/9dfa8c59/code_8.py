def generate_primes(n_max):
    primes = []
    for num in range(2, n_max + 1):
        is_prime = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def generate_permutations(num):
    digits = [int(digit) for digit in str(num)]
    permutations = []
    def permute(i, current):
        if i == len(digits):
            permutations.append(int("".join(map(str, current))))
        else:
            for j in range(i, len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                permute(i + 1, current + [digits[i]])
    permute(0, [])
    return set(permutations)

def find_prime_permutations(n_max, k_perms):
    primes = generate_primes(n_max)
    prime_perm_count = {}
    for prime in primes:
        permutations = generate_permutations(prime)
        prime_perm_count[prime] = len([perm for perm in permutations if is_prime(perm)])
    
    count = 0
    smallest = float("inf")
    largest = float("-inf")
    for prime, count_perm in prime_perm_count.items():
        if count_perm == k_perms:
            if count > 0:
                return [count, smallest, largest]
            count += 1
            smallest = min(smallest, prime)
            largest = max(largest, prime)
    
    return [0, 0, 0]

def is_prime(num):
    if num < 2:
        return False
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True

n_max, k_perms = map(int, input().split())
print(find_prime_permutations(n_max, k_perms))
