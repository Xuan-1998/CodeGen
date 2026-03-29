import sys
from collections import defaultdict

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def even_sum_odd_sum(room_number):
    even_sum = 0
    odd_sum = 0
    while room_number > 0:
        digit = room_number % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        room_number //= 10
    return even_sum, abs(even_sum - odd_sum)

def total_diamonds(n):
    dp = defaultdict(int)
    for i in range(1, n+1):
        for j in range(1, n+1):
            room_number = i * j
            even_sum, odd_sum = even_sum_odd_sum(room_number)
            dp[(i, j)] = abs(even_sum - odd_sum)
    return sum(dp.values())

t = int(input())
for _ in range(t):
    n = int(input())
    print(total_diamonds(n))
