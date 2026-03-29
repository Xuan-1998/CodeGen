def solution(n_max, k_perms):
    primes = generate_primes(n_max)
    prime_permutations = [count_permutations(p) for p in primes]
    count = sum(1 for perm_count in prime_permutations if perm_count == k_perms)

    smallest = largest = 0
    for i, (p, perm_count) in enumerate(zip(primes, prime_permutations)):
        if perm_count == k_perms:
            smallest = p
            largest = p
            break

    return [count, smallest, largest]
