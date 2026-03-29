import sys

def max_grade(n, t):
    # Parse the input decimal fraction and store it as a Python float
    fraction = float(input().strip())

    # Initialize the maximum grade to 0
    max_grade = 0

    # Loop through each digit of the decimal fraction
    for i in range(1, n+1):
        # Calculate the current rounding choice (up or down)
        round_choice = int((fraction * 10**i) % 2)

        # If the time limit is not exceeded, calculate the resulting grade
        if t >= 1:
            grade = int(fraction * 10**i + round_choice / 2)
            max_grade = max(max_grade, grade)
            t -= 1

    return max_grade

# Read input from stdin and print the answer to stdout
n, t = map(int, sys.stdin.readline().split())
print(max_grade(n, t))
