def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_permutations(n):
    digits = [int(d) for d in str(n)]
    perms = []
    def permute(digits, prefix=[]):
        if not digits:
            perms.append(int(''.join(map(str, prefix))))
        else:
            for i, d in enumerate(digits):
                remaining_digits = digits[:i] + digits[i+1:]
                permute(remaining_digits, prefix + [d])
    permute(digits)
    return [p for p in perms if is_prime(p)]

n_max, k_perms = map(int, input().split())
count = 0
smallest = float('inf')
largest = float('-inf')

for p in range(2, n_max):
    if is_prime(p) and len(get_permutations(p)) == k_perms:
        count += 1
        smallest = min(smallest, p)
        largest = max(largest, p)

print([count, smallest, largest])
