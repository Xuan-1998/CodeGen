import sys

def x_sequence_count(N, M, U, L):
    # Sort the radii in ascending order
    U.sort()
    L.sort()

    # Initialize the count of X-sequences
    count = 0

    # Iterate through the arrays to count the number of sequences
    i, j = 0, 0
    while i < N and j < M:
        if U[i] >= L[j]:
            # Count the number of sequences that include the current upper hemisphere
            count += (M - j)
            i += 1
        else:
            # Move to the next lower hemisphere
            j += 1

    return count % (10**9 + 7)

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    print(x_sequence_count(N, M, U, L))
