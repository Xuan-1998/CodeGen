import random

def recursive_sort(n):
    permutation = list(range(1, n+1))  # Initialize the permutation
    x = len(permutation) // 2  # Select the middle element as the pivot

    while True:
        if permutation[x-1] == x:  # If the permutation is already sorted, return it
            return ' '.join(map(str, permutation))

        # Swap the x-th and (x-1)-th elements
        permutation[x-1], permutation[x] = permutation[x], permutation[x-1]

def generate_permutation(n):
    return ' '.join(map(str, random.sample(range(1, n+1), n)))

# Example usage:
n = int(input())  # Read input from standard input
permutation = generate_permutation(n)
print(recursive_sort(int(permutation.split()[0])))  # Print the sorted permutation to standard output
