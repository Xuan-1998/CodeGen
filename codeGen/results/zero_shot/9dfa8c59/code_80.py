import sys

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def permute_digits(n):
    """Generate all possible permutations of the digits of a prime number"""
    digits = [int(d) for d in str(n)]
    perms = []
    def permute(digits, prefix=[]):
        if not digits:
            perms.append(int("".join(map(str, prefix))))
        else:
            for i in range(len(digits)):
                permutation = digits[i]
                remaining_digits = digits[:i] + digits[i+1:]
                permute(remaining_digits, prefix + [permutation])
    permute(digits)
    return [p for p in perms if is_prime(p)]

def main():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    count = 0
    smallest = largest = 0
    for i in range(2, n_max):
        if is_prime(i) and len(permute_digits(i)) == k_perms:
            count += 1
            smallest = min(smallest, i)
            largest = max(largest, i)
    print([count, smallest, largest])

if __name__ == "__main__":
    main()
