def count_diamonds():
    T = int(input())  # Read input, assume T is the number of test cases
    for _ in range(T):
        N = int(input())  # Read grid size N
        total_diamonds = 0  # Initialize total diamonds counter
        for i in range(N):
            for j in range(N):
                room_number = i + j + 1  # Calculate room number
                even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
                diamonds_in_room = abs(even_sum - odd_sum)  # Calculate number of diamonds
                total_diamonds += diamonds_in_room  # Add to total diamonds count

        print(total_diamonds)  # Print result for each test case

count_diamonds()
