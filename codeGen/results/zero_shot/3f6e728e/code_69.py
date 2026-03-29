import sys

def count_x_sequences():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        U_radii = list(map(int, sys.stdin.readline().split()))
        L_radii = list(map(int, sys.stdin.readline().split()))

        # Sort radii in descending order
        U_radii.sort(reverse=True)
        L_radii.sort(reverse=True)

        # Initialize count of sequences
        sequence_count = 1

        # Iterate through the sorted radii to count sequences
        for i in range(len(U_radii)):
            if i < len(L_radii) and U_radii[i] > L_radii[i]:
                sequence_count *= (len(U_radii) - i)
            else:
                break

        print(sequence_count % (10**9 + 7))

count_x_sequences()
