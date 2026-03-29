def get_room_number(row, col):
    return row + col

def get_sum_of_even_odd_digits(room_number):
    even_sum = 0
    odd_sum = 0
    for digit in str(room_number):
        if int(digit) % 2 == 0:  # Even digit
            even_sum += int(digit)
        else:  # Odd digit
            odd_sum += int(digit)
    return abs(even_sum - odd_sum)

def get_total_diamonds(N):
    total_diamonds = 0
    for row in range(1, N+1):
        for col in range(1, N+1):
            room_number = get_room_number(row, col)
            diamond_count = get_sum_of_even_odd_digits(room_number)
            total_diamonds += diamond_count
    return total_diamonds

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_diamonds = get_total_diamonds(N)
    print(total_diamonds)
