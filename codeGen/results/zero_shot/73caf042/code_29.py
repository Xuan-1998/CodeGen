import sys

def count_diamonds(N):
    total_diamonds = 0
    for i in range(1, N+1):
        room_number = i
        even_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
        odd_digits_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
        diamonds_in_room = abs(even_digits_sum - odd_digits_sum)
        total_diamonds += diamonds_in_room
    return total_diamonds

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_diamonds(N))
