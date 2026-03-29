# Step 1: Read input
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Step 2: Count the number of unique radii for each hemisphere
    upper_unique_radii = len(set(U))
    lower_unique_radii = len(set(L))

    # Step 3: Calculate the total number of X-sequences that can be built
    total_sequences = 1
    for i in range(1, C+1):
        if i <= N:
            total_sequences *= (upper_unique_radii - (i-1))
        if i <= M:
            total_sequences *= (lower_unique_radii - (i-1))

    # Step 4: Print the answer modulo 10^9+7
    print(total_sequences % (10**9 + 7))
