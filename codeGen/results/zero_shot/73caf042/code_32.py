import sys

def calculate_diamonds():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        diamonds = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                room_number = i + j
                even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
                diamonds_in_room = abs(even_sum - odd_sum)
                diamonds += diamonds_in_room
        print(diamonds)

calculate_diamonds()
