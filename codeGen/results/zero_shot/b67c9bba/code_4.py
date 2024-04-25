from fractions import Fraction
from math import factorial

def expected_shuffles(n):
    # Base case: if n is 1 or 2, we know the expected shuffles are 0 and 1 respectively
    if n == 1:
        return Fraction(0, 1)
    if n == 2:
        return Fraction(1, 1)

    # For larger n, we need to find a pattern or recursive relationship
    # This is a placeholder for the actual logic to be implemented
    # TODO: Implement the logic to calculate the expected shuffles for n > 2

    # Placeholder return
    return Fraction(1, factorial(n))

# Test the function with small values of n to look for patterns
for i in range(1, 10):
    print(f"Expected shuffles for n={i}: {expected_shuffles(i)}")
