import sys

total_diamonds = 0
T = int(input())

for _ in range(T):
    N = int(input())
    total_room_diamonds = 0
    
    for i in range(1, N + 1):
        room_number = i
        even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
        total_room_diamonds += abs(even_sum - odd_sum)
    
    print(total_room_diamonds)
