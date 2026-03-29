def calculate_diamonds():
    T = int(input())
    total_diamonds = 0

    for _ in range(T):
        N = int(input())
        diamonds_in_grid = 0

        for i in range(1, N+1):
            room_number = i
            even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds_in_room = abs(even_digits_sum - odd_digits_sum)
            diamonds_in_grid += diamonds_in_room

        total_diamonds += diamonds_in_grid

    print(total_diamonds)

calculate_diamonds()
