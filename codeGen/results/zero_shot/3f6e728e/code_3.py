import sys

def count_sequences(N, M, C):
    # Initialize the result array with zeros
    result = [0] * (C + 1)

    # Iterate over the upper hemispheres
    for i in range(N):
        # For each upper hemisphere, iterate over the possible radii
        for j in range(1, C + 1):
            # Update the result array with the product of possibilities
            result[j] += (C - j) ** (M - i)

    return [x % (10**9 + 7) for x in result]

# Read input from stdin
T = int(sys.stdin.readline())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    U = list(map(int, sys.stdin.readline().split()))
    L = list(map(int, sys.stdin.readline().split()))
    
    # Calculate the number of ways to build each X-sequence
    sequences = count_sequences(N, M, C)
    
    # Print the result
    print(' '.join(map(str, sequences)))
