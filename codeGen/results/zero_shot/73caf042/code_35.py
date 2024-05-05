# Initialize total diamonds
total_diamonds = 0

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the size of the grid (N)
    N = int(input())
    
    # Initialize a variable to store the total diamonds for this test case
    test_case_diamonds = 0
    
    # Loop through each room in the grid
    for i in range(1, N+1):
        # Calculate the sum of even digits and odd digits in the room number
        even_digits_sum = sum(int(digit) for digit in str(i) if int(digit) % 2 == 0)
        odd_digits_sum = sum(int(digit) for digit in str(i) if int(digit) % 2 != 0)
        
        # Calculate the absolute difference between the sums
        room_diamonds = abs(even_digits_sum - odd_digits_sum)
        
        # Add the diamonds from this room to the total for this test case
        test_case_diamonds += room_diamonds
    
    # Print the total diamonds for this test case
    print(test_case_diamonds)

# Print the total diamonds across all test cases
print(total_diamonds)
