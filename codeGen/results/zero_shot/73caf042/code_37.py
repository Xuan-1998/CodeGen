def calculate_total_diamonds():
    t = int(input())  # Read T, the number of test cases
    for _ in range(t):
        n = int(input())  # Read N, the size of the grid
        total_diamonds = 0
        for i in range(n):
            for j in range(n):
                room_number = (i + 1) + (j + 1)
                even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
                total_diamonds += abs(even_sum - odd_sum)
        print(total_diamonds)

calculate_total_diamonds()
