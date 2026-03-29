import sys

def generate_permutations(s, k, current):
    if k == 0:
        return {int(current)}
    permutations = set()
    for d in range(10):
        new_current = str(d) + (str(current) if s > 1 else '')
        if s > 1:
            permutations.update(generate_permutations(s - 1, k - 1, new_current))
        else:
            permutations.add(int(new_current))
    return permutations

def has_k_perms(p, k):
    perms = generate_permutations(len(str(p)), k, str(p))
    return len(perms) == k

def main():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    count_of_primes_with_k_perms = 0
    min_prime = max_prime = 0
    for p in range(2, n_max + 1):
        if all(p % i for i in range(2, int(p ** 0.5) + 1)):
            if has_k_perms(p, k_perms):
                count_of_primes_with_k_perms += 1
                min_prime = min(min_prime, p)
                max_prime = max(max_prime, p)
    print([count_of_primes_with_k_perms, min_prime, max_prime])

if __name__ == "__main__":
    main()
