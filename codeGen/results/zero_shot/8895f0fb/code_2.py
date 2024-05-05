import sys

def calculate_expected_carry(t):
    total_non_zero_carries = 0
    for _ in range(t):
        n = int(input())
        total_possibilities = 10**n
        non_zero_carries = 0
        for i in range(n, 0, -1):
            possibilities = [int(x) for x in map(str, range(10))]
            for a in possibilities:
                for b in possibilities:
                    if (a + b) >= 10:
                        non_zero_carries += 1
            total_possibilities //= 10
        expected_carry = non_zero_carries / total_possibilities
        print(f"{expected_carry:.6f}")

if __name__ == "__main__":
    t = int(input())
    calculate_expected_carry(t)
