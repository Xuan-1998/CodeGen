# Receive input for T test cases
T = int(input())

for _ in range(T):
    # Receive N, the size of the grid
    N = int(input())
    
    # Initialize total diamonds to 0
    total_diamonds = 0
    
    # Iterate over each room (row and column) in the grid
    for i in range(1, N+1):
        for j in range(1, N+1):
            # Calculate the room number as the sum of row and column numbers
            room_number = i + j
            
            # Calculate the sum of even digits in the room number
            even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            
            # Calculate the sum of odd digits in the room number
            odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            
            # Calculate the number of diamonds in this room as the absolute difference between even and odd sums
            diamond_count = abs(even_sum - odd_sum)
            
            # Add the diamonds from this room to the total
            total_diamonds += diamond_count
    
    # Print the total number of diamonds for this test case
    print(total_diamonds)
