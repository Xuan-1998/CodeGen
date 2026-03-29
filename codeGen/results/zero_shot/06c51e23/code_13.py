import math

def maximize_grade():
    n = int(input())  # Read length of decimal fraction from stdin
    t = int(input())  # Read time limit from stdin
    decimal_fraction = input()  # Read decimal fraction from stdin

    # Calculate the maximum possible grade by maximizing the number of rounding operations
    max_grade = math.floor(math.log2(t))  # Log2(time limit) will give us the maximum number of rounding operations within the time limit

    print(max_grade)  # Print the maximum possible grade to stdout

maximize_grade()
