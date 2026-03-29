from collections import defaultdict

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    permutations = 1
    digits = str(n)
    for i, digit in enumerate(digits):
        num_options = 9 - (int(digit) - 1)
        if i < len(digits) - 1 and int(digits[i]) <= int(digits[i+1]):
            num_options -= 1
        permutations *= num_options
    return permutations

def is_prime_perm(n, k_perms):
    n_max = int(input())
    k_perms = int(input())
    
    memo = defaultdict(int)
    count = 0
    min_n = float('inf')
    max_n = -float('inf')

    for n in range(2, n_max + 1):
        if is_prime(n):
            permutations = count_permutations(n)
            if permutations == k_perms:
                if n not in memo:
                    memo[n] = True
                else:
                    continue
                
                count += 1
                min_n = min(min_n, n)
                max_n = max(max_n, n)

    return [count, min_n, max_n]
