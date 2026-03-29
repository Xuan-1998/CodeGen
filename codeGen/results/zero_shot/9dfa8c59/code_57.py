import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def get_permutations(n):
    digits = [int(x) for x in str(n)]
    permutations = list(itertools.permutations(digits))
    return [''.join(map(str, p)) for p in permutations]

def count_prime_permutations(n):
    perms = get_permutations(n)
    prime_perms = [p for p in perms if is_prime(int(p))]
    return len(prime_perms)

def find_smallest_largest_prime_numbers(k_perms, n_max):
    count = 0
    smallest = float('inf')
    largest = -float('inf')
    for i in range(2, n_max + 1):
        if count_prime_permutations(i) == k_perms:
            if is_prime(i):
                count += 1
                smallest = min(smallest, i)
                largest = max(largest, i)
    return [count, smallest, largest]

def main():
    n_max, k_perms = map(int, input().split())
    result = find_smallest_largest_prime_numbers(k_perms, n_max)
    print(*result)

if __name__ == "__main__":
    main()
