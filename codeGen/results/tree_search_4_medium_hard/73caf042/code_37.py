# Define the function f(i, j) that returns the total number of diamonds in the i-th row and j-th column.
def f(i, j):
    # Calculate the room number (i + j - 1)
    room_number = i + j - 1
    
    # Calculate the sum of even digits in the room number
    even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
    
    # Calculate the sum of odd digits in the room number
    odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
    
    # The total number of diamonds is the absolute difference between even_sum and odd_sum
    return abs(even_sum - odd_sum)

# Initialize the memo dictionary to store values of f(i, j) for smaller values of i and j.
memo = {0: 0}

# Define a recursive function f(i, j) using the transition relationship:
def dynamic_f(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    
    # Base case: when i or j equals N, return 0
    if i == N or j == N:
        return 0
    
    # Calculate f(i, j) using the transition relationship:
    room_number = i + j - 1
    even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
    
    memo[(i, j)] = abs(even_sum - odd_sum) + dynamic_f(i-1, j-1)
    
    return memo[(i, j)]

# Read the input T from stdin
T = int(input())

# Calculate and print the total number of diamonds for each test case
for _ in range(T):
    N = int(input())
    total_diamonds = 0
    
    # Iterate from i = 1 to N and j = 1 to N, add up f(i, j)
    for i in range(1, N+1):
        for j in range(1, N+1):
            total_diamonds += dynamic_f(i, j)
    
    print(total_diamonds)
