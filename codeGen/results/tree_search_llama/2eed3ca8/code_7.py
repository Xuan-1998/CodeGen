from collections import defaultdict

def is_circular_sequence(sequence):
    n = len(sequence)
    
    # Create a hash table with default values as 0
    hash_table = defaultdict(int)
    for i in range(n):
        if sequence[i] == 'F':  # F represents forward movement
            new_index = (i + 1) % n
        elif sequence[i] == 'L':  # L represents left turn
            new_index = (i - 1) % n
        else:  # R represents right turn
            new_index = (i + 1) % n
        
        if hash_table[new_index]:
            return "Circular"
        
        hash_table[i] = 1
    
    return "Not Circular"

# Read input from standard input
sequence = input()

# Check if the sequence is circular
print(is_circular_sequence(sequence))
