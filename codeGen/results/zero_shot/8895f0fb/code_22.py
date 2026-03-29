import sys

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_carry_count = 0
        for i in range(10):
            for j in range(10):
                # Calculate the number of carries for this pair of digits
                if (i + j) >= 10:
                    carry_count = 1
                else:
                    carry_count = 0
                total_carry_count += carry_count
        expected_carries = total_carry_count / (N ** 2)
        print(expected_carries)

calculate_expected_carries()
