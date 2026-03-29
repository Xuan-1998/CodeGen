import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    def permute(digits):
        if len(digits) == 1:
            permutations.add(int(''.join(map(str, digits))))
        else:
            for i in range(len(digits)):
                remaining_digits = digits[:i] + digits[i+1:]
                for p in permute(remaining_digits):
                    permutations.add(int(str(digits[i]) + str(p)))
    permute(digits)
    return permutations

def solve():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    count = 0
    smallest_prime = None
    largest_prime = None
    
    for i in range(2, n_max):
        if is_prime(i):
            perms = prime_permutations(i)
            if len(perms) == k_perms:
                count += 1
                if smallest_prime is None or i < smallest_prime:
                    smallest_prime = i
                if largest_prime is None or i > largest_prime:
                    largest_prime = i
    
    print([count, smallest_prime, largest_prime])

if __name__ == "__main__":
    solve()
