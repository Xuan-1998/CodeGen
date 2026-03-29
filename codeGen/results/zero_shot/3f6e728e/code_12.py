import sys

# Input: T test cases
T = int(input())

for _ in range(T):
    N, M, C = map(int, input().split())
    upper_radii = list(map(int, input().split()))
    lower_radii = list(map(int, input().split()))

    unique_sequences = set()

    for i in range(N):
        for j in range(M):
            sequence = tuple(sorted([upper_radii[i], lower_radii[j]]))
            if sequence not in unique_sequences:
                unique_sequences.add(sequence)

    # Calculate the result modulo 10^9+7
    result = len(unique_sequences) % (10**9 + 7)
    print(result, end=' ')
