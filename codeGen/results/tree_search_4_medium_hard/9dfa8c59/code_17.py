import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    digits = [int(i) for i in str(n)]
    permutations = set()
    def permute(index):
        if index == len(digits):
            permutations.add(tuple(sorted(digits)))
            return
        for i in range(len(digits)):
            digits[i], digits[index] = digits[index], digits[i]
            permute(index + 1)
            digits[i], digits[index] = digits[index], digits[i]

    permute(0)
    return len([p for p in permutations if is_prime(int(''.join(map(str, p))))])

def main():
    n_max, k_perms = map(int, input().split())
    prime_counts = {}
    for i in range(2, n_max):
        if not is_prime(i):
            continue
        count = count_permutations(i)
        if count == k_perms:
            prime_counts[i] = 1

    if len(prime_counts) > 0:
        print([len(prime_counts), min(prime_counts.keys()), max(prime_counts.keys())])
    else:
        print([0, 0, 0])

if __name__ == "__main__":
    main()
