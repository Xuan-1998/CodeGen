import sys

def calculate_expected_carries():
    t = int(input())  # Read T from stdin
    for _ in range(t):
        n = int(input())  # Read N from stdin
        total_carries = 0  # Initialize counter for total carries
        for i in range(n):
            for j in range(10):  # Iterate over each digit value (0-9)
                for k in range(10):  # Iterate over each digit value (0-9)
                    # Check if adding the digits results in a sum >= 10
                    if j + k >= 10:
                        total_carries += 1  # Increment counter for carries
        expected_carries = total_carries / (10 ** n)  # Calculate expected number of carries
        print(f"{expected_carries:.6f}")  # Print the result to stdout

calculate_expected_carries()
