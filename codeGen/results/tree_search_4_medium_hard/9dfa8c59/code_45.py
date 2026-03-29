import itertools

def get_permutations(n):
    return len(list(itertools.permutations(str(n))))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def dp(n_ max, k_perms):
    count = 0
    smallest_prime = float('inf')
    largest_prime = 0

    for n in range(2, n_max):
        if is_prime(n):
            permutations = get_permutations(n)
            if permutations == k_perms:
                count += 1
                smallest_prime = min(smallest_prime, n)
                largest_prime = max(largest_prime, n)

    return [count, smallest_prime, largest_prime]


if __name__ == "__main__":
    n_max, k_perms = map(int, input().split())
    result = dp(n_max, k_perms)
    print(result[0], result[1], result[2])
