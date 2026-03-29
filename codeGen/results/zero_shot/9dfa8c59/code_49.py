def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    digits = [int(x) for x in str(n)]
    permutations = []
    def permute(current, remaining):
        if not remaining:
            permutations.append(int(''.join(map(str, current))))
        else:
            for i in range(len(remaining)):
                c = remaining[i]
                remaining.pop(i)
                permute(current + [c], remaining)
                remaining.insert(i, c)
    permute([], digits)
    return set(permutations)

def find_prime_numbers(n_max, k_perms):
    result = []
    for n in range(2, n_max + 1):
        if is_prime(n):
            perms = permute_digits(n)
            count = sum(is_prime(p) for p in perms)
            if count == k_perms:
                result.append((n, len(min(map(str, perms))), len(max(map(str, perms)))))
    return [len(result), *min(result, default=[0, 0, 0]), *max(result, default=[0, 0, 0])]

n_max, k_perms = map(int, input().split())
print(*find_prime_numbers(n_max, k_perms))
