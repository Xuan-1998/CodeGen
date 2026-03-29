import sys

def calculate_diamonds(n):
    total_diamonds = 0
    for i in range(1, n+1):
        room_number = i + (i-1)
        even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
        diamonds = abs(even_sum - odd_sum)
        total_diamonds += diamonds
    return total_diamonds

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(calculate_diamonds(n))
