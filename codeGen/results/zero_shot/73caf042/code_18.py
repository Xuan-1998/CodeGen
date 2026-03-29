def count_diamonds():
    T = int(input())  # Input number of test cases
    for _ in range(T):
        N = int(input())  # Input size of the grid (N x N)
        total_diamonds = 0
        for i in range(1, N+1):  # Iterate over each room
            room_number = i
            even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds_in_room = abs(even_sum - odd_sum)
            total_diamonds += diamonds_in_room
        print(total_diamonds)

count_diamonds()
