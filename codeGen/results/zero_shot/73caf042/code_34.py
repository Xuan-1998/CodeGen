import sys

def calculate_room_numbers(N):
    total_rooms = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            room_number = i + j
            # Do something with the room number...
            total_rooms += 1
    return total_rooms

def calculate_diamonds_per_room(room_number):
    even_digits_sum = 0
    odd_digits_sum = 0
    for digit in str(room_number):
        if int(digit) % 2 == 0:
            even_digits_sum += int(digit)
        else:
            odd_digits_sum += int(digit)
    return abs(even_digits_sum - odd_digits_sum)

def calculate_total_diamonds(N):
    total_diamonds = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            room_number = i + j
            diamonds_in_room = calculate_diamonds_per_room(room_number)
            total_diamonds += diamonds_in_room
    return total_diamonds

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_total_diamonds(N))
