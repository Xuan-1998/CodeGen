import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_diamonds = 0
    for i in range(N):
        for j in range(N):
            room_number = (i + 1) + (j + 1)
            even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds_in_room = abs(even_digits_sum - odd_digits_sum)
            total_diamonds += diamonds_in_room
    print(total_diamonds)
