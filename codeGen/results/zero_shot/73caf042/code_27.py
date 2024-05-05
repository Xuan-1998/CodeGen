import sys

def calculate_diamonds(n):
    total_diamonds = 0
    for i in range(n):
        for j in range(n):
            room_number = i + j
            even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            diamonds_in_room = abs(even_sum - odd_sum)
            total_diamonds += diamonds_in_room
    return total_diamonds

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(calculate_diamonds(n))
