from itertools import permutations
import sys

def prime_perms(n_max, k_perms):
    dp = {}
    count_smallest_largest = [0, 0, 0]
    
    for i in range(2, n_max+1):
        if is_prime(i):
            perms_count = sum(1 for p in permutations(str(i)) if int(''.join(p)) <= k_perms)
            dp[i] = perms_count
            if perms_count == k_perms:
                count_smallest_largest[0] += 1
                count_smallest_largest[1] = min(count_smallest_largest[1], i)
                count_smallest_largest[2] = max(count_smallest_largest[2], i)
    
    return [count_smallest_largest[0], count_smallest_largest[1], count_smallest_largest[2]]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n_max, k_perms = map(int, sys.stdin.read().split())
    result = prime_perms(n_max, k_perms)
    print(*result, sep='\n')
