import itertools

def generate_prime_numbers(n_max):
    primes = [2]
    for p in range(3, n_max + 1):
        is_prime = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
    return primes

def count_k_perms_primes(k_perms, n_max):
    prime_count = 0
    min_prime = float('inf')
    max_prime = 0
    for p in generate_prime_numbers(n_max):
        digit_permutations = [''.join(p) + ''.join(map(str, i)) for i in itertools.permutations(map(int, str(p))) if int(''.join(i)) <= n_max]
        k_perms_found = sum(1 for _ in filter(lambda x: int(x) in generate_prime_numbers(n_max), digit_permutations))
        if k_perms == k_perms_found:
            prime_count += 1
            min_prime = min(min_prime, p)
            max_prime = max(max_prime, p)
    return [prime_count, min_prime, max_prime]

n_max, k_perms = map(int, input().split())
print(count_k_perms_primes(k_perms, n_max))
