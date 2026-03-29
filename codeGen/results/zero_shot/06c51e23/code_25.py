import sys

def max_grade(n, t, fraction):
    # Initialize the maximum grade and the current index
    max_grade = 0
    i = n - 1

    while i >= 0 and t > 0:
        # Check if we can round up or down at this position
        if fraction[i] == '9':
            # If the digit is 9, we cannot round up, so try to round down
            if t >= 1:
                max_grade += 1
                t -= 1
        else:
            # If the digit is not 9, we can round up or down
            if t >= 2:
                max_grade += 2
                t -= 2

        i -= 1

    return max_grade

# Read inputs from stdin
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = sys.stdin.readline().strip()

# Call the max_grade function and print the result to stdout
print(max_grade(n, t, fraction))
