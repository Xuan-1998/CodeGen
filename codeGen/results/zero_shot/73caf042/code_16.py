import sys

def count_diamonds(n):
    total_diamonds = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            room_number = i + j
            even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds_in_room = abs(even_digits_sum - odd_digits_sum)
            total_diamonds += diamonds_in_room
    return total_diamonds

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_diamonds(n))
