===BEGIN CODE===
import sys

def get_unique_sums(set_of_integers):
    unique_sums = set()  # Initialize an empty set for unique sums
    subsets = []  # Initialize an empty list for all possible subsets
    
    # Generate all possible subsets of the given set
    import itertools
    for r in range(len(set_of_integers) + 1):
        subsets.extend(itertools.combinations(set_of_integers, r))
    
    # Calculate and store the sum of each subset
    for subset in subsets:
        unique_sums.add(sum(subset))  # Add the sum to the set of unique sums
    
    return sorted(list(unique_sums))  # Return the list of unique sums


# Read input from stdin
input_line = sys.stdin.readline()
N, *set_of_integers = map(int, input_line.split())

unique_sums = get_unique_sums(set_of_integers)
print(' '.join(map(str, unique_sums)))  # Print the list of unique sums

===END CODE===
