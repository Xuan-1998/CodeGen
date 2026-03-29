import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_pairs = 10 ** N  # Calculate the total number of pairs
        expected_carries = 0
        for i in range(N):
            for j in range(10):  # Loop through all possible digits in A and B
                if (i + j) >= 10:  # Check if there's a carry
                    expected_carries += 1
        print(expected_carries / total_pairs)

calculate_expected_carries()
