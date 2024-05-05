def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_permutations(n):
    # implementation pending
    pass

n_max = int(input())
k_perms = int(input())

prime_count = 0
smallest_prime = None
largest_prime = None

for n in range(2, n_max + 1):  # iterate through numbers below n_max
    permutations = get_permutations(n)  # generate permutations for this number
    if len(permutations) == k_perms:  # check if the number has exactly k_perms prime permutations
        if is_prime(n):
            prime_count += 1
            if smallest_prime is None or n < smallest_prime:
                smallest_prime = n
            if largest_prime is None or n > largest_prime:
                largest_prime = n

print([prime_count, smallest_prime, largest_prime])
