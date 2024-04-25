from fractions import Fraction

# Recursive function to calculate expected shuffles
def expected_shuffles(i, n, memo):
    if i == n - 1:
        return 1
    if memo[i] != -1:
        return memo[i]

    expected_sum = 0
    # Calculate the sum of expected shuffles for all possible outcomes of the next shuffle
    for j in range(i + 1, n):
        expected_sum += expected_shuffles(j, n, memo)

    # Calculate the expected shuffles for the current subproblem
    expected = 1 + Fraction(expected_sum, n - i)
    memo[i] = expected
    return expected

# Main function to handle the input and output
def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the number of elements in the sequence
        memo = [-1 for _ in range(n)]  # Initialize memoization table
        result = expected_shuffles(0, n, memo)  # Calculate the expected number of shuffles
        print(f"{result.numerator}/{result.denominator}")  # Print the result as an irreducible fraction

# Run the main function
if __name__ == "__main__":
    main()
