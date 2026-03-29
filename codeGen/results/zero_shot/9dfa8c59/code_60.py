import sys

def sieve_of_eratosthenes(n_max):
    is_prime = [True] * (n_max + 1)
    is_prime[0] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n_max + 1, i):
                is_prime[j] = False
    return [p for p in range(2, n_max + 1) if is_prime[p]]

def is_prime_permutation(p, k_perms):
    # Rearrange the digits of p to form new numbers
    prime_perms = set()
    for _ in range(k_perms):
        perms = int(''.join(sorted(str(p))))
        if perms != p and perms < n_max:
            prime_perms.add(perms)
    return len(prime_perms) == k_perms

def main():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    primes = sieve_of_eratosthenes(n_max)
    count_list = []
    for p in primes:
        if is_prime_permutation(p, k_perms):
            count_list.append(p)
    if not count_list:
        return [0, 0, 0]
    print([len(count_list), min(count_list), max(count_list)])

if __name__ == "__main__":
    main()
