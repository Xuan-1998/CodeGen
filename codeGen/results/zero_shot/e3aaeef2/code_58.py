import sys

def solve(n, m):
    # Initialize a variable to keep track of the number of digits in the result
    result_digits = len(str(n))

    for _ in range(m):
        # Convert the current number to a string and iterate through each digit
        str_n = str(n)
        new_digits = 0

        for d in str_n:
            # Replace each digit with its incremented value (d + 1) and count the new digits
            new_digit = int(d) + 1
            if new_digit > 9:  # If the incremented digit is greater than 9, it becomes a two-digit number
                new_digits += 2
            else:
                new_digits += 1

        # Update the result with the new digits count
        result_digits = new_digits

    return result_digits % (10**9 + 7)

t = int(input())  # Read the number of test cases

for _ in range(t):
    n, m = map(int, input().split())  # Read the initial number and operations for each test case
    print(solve(n, m))  # Apply the solution and print the result modulo 10^9+7
