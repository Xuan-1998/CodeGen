def calculate_diamonds(n):
    total_diamonds = 0
    for row in range(1, n+1):
        for col in range(1, n+1):
            room_number = row + col
            even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds_per_room = abs(even_digits_sum - odd_digits_sum)
            total_diamonds += diamonds_per_room
    return total_diamonds

n = int(input())
print(calculate_diamonds(n))
