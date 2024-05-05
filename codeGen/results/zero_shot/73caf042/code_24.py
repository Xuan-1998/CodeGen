import sys

def count_diamonds():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_diamonds = 0
        for i in range(1, N**2 + 1):
            room_number = str(i)
            even_digits_sum = sum(int(digit) for digit in room_number if int(digit) % 2 == 0)
            odd_digits_sum = sum(int(digit) for digit in room_number if int(digit) % 2 != 0)
            diamonds_in_room = abs(even_digits_sum - odd_digits_sum)
            total_diamonds += diamonds_in_room
        print(total_diamonds)

count_diamonds()
