def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    digits = [int(x) for x in str(n)]
    perms = []
    def permute(digits, prefix=[]):
        if not digits:
            perms.append(int(''.join(map(str, prefix))))
        else:
            for i in range(len(digits)):
                remaining_digits = digits[:i] + digits[i+1:]
                permute(remaining_digits, prefix + [digits[i]])
    permute(digits)
    return perms

def solve(n_max, k_perms):
    count = 0
    smallest = float('inf')
    largest = float('-inf')

    for i in range(2, n_max):
        if is_prime(i):
            perms = permute_digits(i)
            if len([p for p in perms if is_prime(p)]) == k_perms:
                count += 1
                smallest = min(smallest, i)
                largest = max(largest, i)

    return [count, smallest, largest]

if __name__ == "__main__":
    n_max = int(input())
    k_perms = int(input())
    result = solve(n_max, k_perms)
    print(*result, sep=' ')
