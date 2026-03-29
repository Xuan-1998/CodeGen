import sys

def even_sum(n):
    return sum(int(digit) for digit in str(n) if int(digit) % 2 == 0)

def odd_sum(n):
    return sum(int(digit) for digit in str(n) if int(digit) % 2 != 0)

total_diamonds = 0
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for row in range(N):
        for column in range(N):
            room_number = row + column + 1
            diamond_count = abs(even_sum(room_number) - odd_sum(room_number))
            total_diamonds += diamond_count

print(total_diamonds)
