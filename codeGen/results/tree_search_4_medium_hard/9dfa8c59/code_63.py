def get_prime_permutations(n_max, k_perms):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_permutations(n):
        perm_count = 0
        for p in range(len(str(n)), 0, -1):
            for digits in itertools.permutations(map(int, str(n)), p):
                num = int(''.join(map(str, digits)))
                if is_prime(num) and perm_count < k_perms:
                    perm_count += 1
                elif perm_count == k_perms:
                    return perm_count
        return perm_count

    count = 0
    smallest = float('inf')
    largest = -float('inf')

    for n in range(n_max, 2, -1):
        if is_prime(n) and get_permutations(n) == k_perms:
            count += 1
            smallest = min(smallest, n)
            largest = max(largest, n)

    return [count, smallest, largest]

n_max, k_perms = map(int, input().split())
print(get_prime_permutations(n_max, k_perms))
