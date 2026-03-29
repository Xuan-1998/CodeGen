import math

def solve(n):
    # Calculate the number of possible combinations
    total_combinations = 2 ** (n - 1)

    # Initialize the count of valid combinations
    valid_combinations = 0

    for i in range(total_combinations):
        combination = bin(i)[2:].zfill(n - 1)
        has_signal_0 = False
        has_signal_n_plus_1 = False
        signal_towns = set()

        # Check the constraints
        for j, bit in enumerate(combination):
            if bit == '1':
                signal_towns.add(j + 1)

        if not signal_towns:
            has_signal_0 = True

        if len(signal_towns) != n:
            has_signal_n_plus_1 = True

        # Check the constraint for town $n+1$
        if has_signal_n_plus_1:
            valid_combinations += 1
            break

    probability = math.factorial(n - 1) * (valid_combinations / total_combinations)
    return int(probability % 998244353)

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
