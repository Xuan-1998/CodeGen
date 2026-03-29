import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    def backtrack(first=0):
        if len(digits) == first:
            permutation = int("".join(map(str, digits)))
            if is_prime(permutation):
                permutations.add(permutation)
        else:
            for i in range(len(digits)):
                digits[0], digits[i] = digits[i], digits[0]
                backtrack(first + 1)
                digits[0], digits[i] = digits[i], digits[0]

    backtrack()
    return permutations

def main():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    count = 0
    min_prime = max_prime = 0
    for i in range(2, n_max):
        if is_prime(i):
            perms = generate_permutations(i)
            if len(perms) == k_perms:
                count += 1
                min_prime = min(min_prime, i)
                max_prime = max(max_prime, i)

    print([count, min_prime, max_prime])

if __name__ == "__main__":
    main()
