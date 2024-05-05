from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def perm_count(p, k_perms):
    count = 0
    for _ in range(len(str(p))):
        perms = set()
        for p in itertools.permutations(map(int, str(p))):
            if is_prime(int(''.join(map(str, p)))):
                perms.add(int(''.join(map(str, p))))
        if len(perms) == k_perms:
            count += 1
    return count

def main():
    n_max = int(input())
    k_perms = int(input())

    prime_nums = set()
    for i in range(2, n_max + 1):
        if is_prime(i):
            prime_nums.add(i)

    perm_counts = {}
    for p in prime_nums:
        perm_counts[p] = perm_count(p, k_perms)

    count = sum(1 for c in perm_counts.values() if c == k_perms)
    min_p, max_p = min((p for p, c in perm_counts.items() if c == k_perms)), max((p for p, c in perm_counts.items() if c == k_perms))

    print(count, min_p, max_p)

if __name__ == "__main__":
    main()
