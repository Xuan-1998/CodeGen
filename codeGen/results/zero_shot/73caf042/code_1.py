def find_total_diamonds():
    T = int(input())  # Read test cases from stdin
    for _ in range(T):
        N = int(input())  # Read grid size from stdin
        total_diamonds = 0
        for i in range(1, N + 1):
            room_number = i + (i % 2) - 1  # Calculate room number as sum of row and column numbers
            even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds = abs(even_digits_sum - odd_digits_sum)
            total_diamonds += diamonds
        print(total_diamonds)  # Print the total number of diamonds to stdout

find_total_diamonds()
