import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_permutations(digits):
    permutations = []
    def permute(arr):
        if len(arr) == 1:
            permutations.append(int(''.join(map(str, arr))))
        else:
            for i in range(len(arr)):
                m = arr[i]
                rem = arr[:i] + arr[i+1:]
                if len(rem) > 0:
                    permute(rem)
                else:
                    permutations.append(m)
    permute(digits)
    return permutations

def count_prime_permutations(n_max, k_perms):
    prime_count = [0, float('inf'), float('inf')]
    for n in range(2, n_max + 1):
        if is_prime(n):
            digits = [int(d) for d in str(n)]
            perms = generate_permutations(digits)
            if len(set(map(int, perms))) == k_perms:
                prime_count[0] += 1
                prime_count[1] = min(prime_count[1], n)
                prime_count[2] = max(prime_count[2], n)
    return [prime_count[0], prime_count[1], prime_count[2]]

n_max, k_perms = map(int, input().split())
print(count_prime_permutations(n_max, k_perms))
