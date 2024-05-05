def x_sequences(N, M, U, L):
    # Count the number of different radii for upper hemispheres
    unique_radii_upper = set(U)
    
    # Count the number of different radii for lower hemispheres
    unique_radii_lower = set(L)
    
    # Combine the counts to find the total number of X-sequences
    x_sequences = len(unique_radii_upper) * len(unique_radii_lower)
    
    return x_sequences

# Read input from stdin
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    
    # Calculate the number of X-sequences for this test case
    x_sequences = x_sequences(N, M, U, L)
    
    # Print the result to stdout
    print(*[x_sequences % (10**9 + 7)])


