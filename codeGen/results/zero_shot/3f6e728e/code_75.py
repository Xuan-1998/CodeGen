import itertools

def count_sequences(u, l):
    # Create a list of all possible sequences
    sequences = []
    for r in range(min(u, l), 0, -1):
        if u >= r and l >= r:
            sequences.append(r)
    return len(sequences)

# Example usage
u = [3, 2, 1]
l = [4, 5, 6]
print(count_sequences(*zip(*[list(x) for x in zip(u, l)])))
