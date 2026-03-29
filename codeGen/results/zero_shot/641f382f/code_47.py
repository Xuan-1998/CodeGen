from math import gcd
from sys import stdin

# Function to read input and find minimum operations
def find_min_operations():
    n = int(stdin.readline().strip())  # Read the number of elements
    array = list(map(int, stdin.readline().strip().split()))  # Read the array elements

    # Check if there is any element that is already 1
    if 1 in array:
        print(n - array.count(1))  # The number of operations is n minus the count of 1s
        return

    # Initialize a variable to store if we can make all elements 1
    can_make_all_ones = False

    # Check pairs of adjacent elements to find if any have GCD equal to 1
    for i in range(n - 1):
        if gcd(array[i], array[i + 1]) == 1:
            can_make_all_ones = True
            break

    # If we cannot make all elements 1, print -1
    if not can_make_all_ones:
        print(-1)
    else:
        # If we can make all elements 1, the minimum operations is n - 1
        print(n - 1)

# Call the function to find the minimum operations
find_min_operations()
