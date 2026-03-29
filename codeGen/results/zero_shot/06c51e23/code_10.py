import sys

def calculate_max_grade(n, t):
    # Initialize the max grade and current decimal value
    max_grade = 0
    decimal_value = float(input().strip())

    while t > 0:
        # Find the first digit after the decimal point that can be rounded up
        for i in range(1, n + 1):
            if int((decimal_value * 10**i) % 10) >= 5:
                # Round up and update max grade
                max_grade = int(decimal_value * 10**i)
                break

        # Check if the rounded value exceeds the time limit
        t -= (max_grade - int(decimal_value))

        # Update decimal value for the next iteration
        decimal_value = (decimal_value + (1 / 10**n)) % 1

    return max_grade

# Read input and calculate max grade
n, t = map(int, sys.stdin.readline().split())
print(calculate_max_grade(n, t))
