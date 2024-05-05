import sys

def digit_sum(n):
    even_digits = sum(int(digit) for digit in str(n) if int(digit) % 2 == 0)
    odd_digits = sum(int(digit) for digit in str(n) if int(digit) % 2 != 0)
    return abs(even_digits - odd_digits)

def total_diamonds(n):
    total_diamonds = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            room_number = i + j
            total_diamonds += digit_sum(room_number)
    return total_diamonds

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(total_diamonds(n))
