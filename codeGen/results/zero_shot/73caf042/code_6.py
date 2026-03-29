import sys

def calculate_room_diamonds(room_number):
    even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
    odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
    return abs(even_digits_sum - odd_digits_sum)

def calculate_total_diamonds(N):
    total_diamonds = 0
    for i in range(1, N + 1):
        room_number = i * (i + 1) // 2
        total_diamonds += calculate_room_diamonds(room_number)
    return total_diamonds

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_total_diamonds(N))
