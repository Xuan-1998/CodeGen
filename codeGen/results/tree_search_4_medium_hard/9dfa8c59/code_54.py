from collections import defaultdict
from itertools import permutations

def count_prime_numbers(n_max, k_perms):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_permutations(num):
        perms = set(str(num))
        permutations_list = list(permutations(perms))
        return len([p for p in permutations_list if int(''.join(map(str, p))) <= n_max and is_prime(int(''.join(map(str, p))))])

    memo = defaultdict(int)
    count = 0
    min_prime = float('inf')
    max_prime = 0

    for num in range(2, n_max + 1):
        if not memo[num]:
            num_permutations = count_permutations(num)
            if num_permutations == k_perms:
                if is_prime(num):
                    count += 1
                    min_prime = min(min_prime, num)
                    max_prime = max(max_prime, num)
            memo[num] = num_permutations

    return [count, min_prime, max_prime]

n_max, k_perms = map(int, input().split())
print(count_prime_numbers(n_max, k_perms))
