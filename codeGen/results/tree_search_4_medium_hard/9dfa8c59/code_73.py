def count_prime_permutations(n_max, k_perms):
    # Initialize counts for smallest, largest, and total prime numbers with k_perms permutations
    smallest, largest, total = 0, 0, 0

    # Iterate through all numbers up to n_max
    for n in range(2, n_max+1):
        # Check if the number is prime
        if is_prime(n):
            # Count the number of permutations that are less than or equal to k_perms
            perms_count = count_permutations(n)
            if perms_count <= k_perms:
                total += 1
                smallest = min(smallest, n)
                largest = max(largest, n)

    return [total, smallest, largest]


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_permutations(num):
    # Initialize a list to store the permutations
    perms = [True] * len(str(num))

    # Iterate through each digit of the number
    for i, d in enumerate(str(num)):
        # Calculate the number of permutations that include this digit at position i
        new_perms = 0
        for j in range(len(str(num))):
            if j != i:
                new_perms += perms[j]
        perms[i] = new_perms

    # Return the total count of permutations
    return sum(perms)


# Read input from standard input
n_max, k_perms = map(int, input().split())

# Print output to standard output
print(count_prime_permutations(n_max, k_perms))
