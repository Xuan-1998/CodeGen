import math

def calculate_factorial():
    t = int(input())  # Read number of test cases from input
    for _ in range(t):
        n = int(input())  # Read the integer 'n' from input
        factorial = math.gamma(n + 1)  # Calculate the gamma function value
        print(int(factorial))  # Print the result

calculate_factorial()
