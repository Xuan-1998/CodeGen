import sys

def generate_primes(n_max):
    primes = []
    for i in range(2, n_max + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def get_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = set()
    def permute(index, current):
        if index == len(digits):
            permutation = int("".join(map(str, current)))
            permutations.add(permutation)
        else:
            for i in range(len(digits)):
                if not index or digits[i] != digits[index - 1]:
                    digits[index - 1], digits[i] = digits[i], digits[index - 1]
                    permute(index + 1, current + [digits[index - 1]])
                    digits[index - 1], digits[i] = digits[i], digits[index - 1]

    permute(0, [])
    return permutations

def solve(n_max, k_perms):
    primes = generate_primes(n_max)
    prime_perm_counts = {}
    min_prime = float('inf')
    max_prime = 0
    for n in primes:
        perms = get_permutations(n)
        if len(perms) == k_perms:
            prime_perm_counts[n] = len(perms)
            min_prime = min(min_prime, n)
            max_prime = max(max_prime, n)

    count = sum(1 for count in prime_perm_counts.values() if count == k_perms)
    return [count, min_prime, max_prime]

if __name__ == "__main__":
    n_max, k_perms = map(int, sys.stdin.read().split())
    print(solve(n_max, k_perms))
