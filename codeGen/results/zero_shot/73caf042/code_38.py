import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_diamonds = 0
    for room_num in range(1, N*N+1):
        even_digits_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 == 0)
        odd_digits_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 != 0)
        diamonds_per_room = abs(even_digits_sum - odd_digits_sum)
        total_diamonds += diamonds_per_room
    print(total_diamonds)
