import sys

def calculate_diamonds(n):
    total_diamonds = 0
    for i in range(1, n+1):
        room_number = (i + i//2)  # Calculate room number as sum of row and column numbers
        even_digits_sum = 0
        odd_digits_sum = 0
        for digit in str(room_number):  # Convert room number to string and iterate over digits
            if int(digit) % 2 == 0:  # Even digit?
                even_digits_sum += int(digit)
            else:
                odd_digits_sum += int(digit)
        diamonds = abs(even_digits_sum - odd_digits_sum)  # Calculate diamonds in this room
        total_diamonds += diamonds  # Add to the total
    return total_diamonds

t = int(sys.stdin.readline())  # Read number of test cases from stdin
for _ in range(t):
    n = int(sys.stdin.readline())
    print(calculate_diamonds(n))  # Print the total number of diamonds for each test case
