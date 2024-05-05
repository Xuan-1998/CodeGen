import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        expected_carries = 0.0
        for i in range(10):
            for j in range(10):
                # Calculate the carry from adding digit i of A and digit j of B
                if (i + j) >= 10:
                    expected_carries += 1.0
        expected_carries /= 100.0  # Divide by total number of pairs
        print("%.6f" % expected_carries)

calculate_expected_carries()
