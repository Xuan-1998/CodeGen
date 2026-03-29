# Step 1: Read input
n_max, k_perms = map(int, input().split())

# Step 2: Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Step 3: Function to generate prime permutations of a number
def get_prime_permutations(num):
    prime_perms = set()
    for _ in range(len(str(num))):
        perms = set()
        for p in itertools.permutations(str(num)):
            num_perm = int(''.join(p))
            if is_prime(num_perm):
                perms.add(num_perm)
        prime_perms.update(perms)
    return len(prime_perms)

# Step 4: Count prime numbers with k_perms below n_max
count = 0
smallest = float('inf')
largest = -float('inf')
for i in range(2, n_max):
    if is_prime(i) and get_prime_permutations(i) == k_perms:
        count += 1
        smallest = min(smallest, i)
        largest = max(largest, i)

# Step 5: Print the result
print([count, smallest, largest])
