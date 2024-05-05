import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_permutations(n_max, k_perms):
    count = 0
    smallest = float('inf')
    largest = -1

    for i in range(2, n_max+1):
        if is_prime(i):
            perms = []
            for p in itertools.permutations(str(i)):
                perm = int(''.join(p))
                if is_prime(perm) and len([j for j in range(2, perm**0.5 + 1) if perm % j == 0]) == 0:
                    perms.append(perm)
            if len(perms) == k_perms:
                count += 1
                smallest = min(smallest, i)
                largest = max(largest, i)

    return [count, smallest, largest]

if __name__ == "__main__":
    n_max = int(input())
    k_perms = int(input())
    result = count_prime_permutations(n_max, k_perms)
    print(result[0])
    print(result[1])
    print(result[2])

