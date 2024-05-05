import math
from collections import defaultdict

def is_prime(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            memo[n] = False
            return False
    memo[n] = True
    return True

def count_permutations(n):
    perm_set = set()
    for p in str(n):
        perm_set.add(int(''.join(sorted(p))))
    return len(perm_set)

def solve():
    n_max, k_perms = map(int, input().split())
    prime_count = 0
    smallest = largest = 0
    for i in range(2, n_max + 1):
        if is_prime(i):
            perms = count_permutations(i)
            if perms == k_perms:
                prime_count += 1
                if not smallest:
                    smallest = i
                largest = i
            elif perms > k_perms:
                break

    print([prime_count, smallest, largest])

if __name__ == "__main__":
    solve()
