from math import gcd
from functools import reduce

def find_gcd(list):
    x = reduce(gcd, list)
    return x

def calculate_expected_shuffles(n):
    # For now, we will assume that each shuffle has an equal chance of sorting the sequence.
    # This is a placeholder for the actual logic that we need to figure out.
    # Since we do not have the actual logic yet, we return "1/1" as a placeholder.
    return "1/1"

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the value of n for each test case
        result = calculate_expected_shuffles(n)
        print(result)

if __name__ == "__main__":
    main()
