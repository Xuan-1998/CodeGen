import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    digits = [int(d) for d in str(n)]
    permutations = []
    def permute(i):
        if i >= len(digits):
            permutations.append(int(''.join(map(str, digits))))
        else:
            for j in range(i, len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                permute(i + 1)
                digits[i], digits[j] = digits[j], digits[i]
    permute(0)
    return permutations

def solve(n_max, k_perms):
    count = 0
    smallest = float('inf')
    largest = float('-inf')

    for i in range(2, n_max + 1):
        if is_prime(i):
            perms = permute_digits(i)
            if len(set(perms)) == k_perms:
                count += 1
                smallest = min(smallest, i)
                largest = max(largest, i)

    return [count, smallest, largest]

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

result = solve(n_max, k_perms)
print(*result, sep=',')
