import sys

def get_even_odd_sum(room_number):
    even_sum = 0
    odd_sum = 0
    
    for digit in str(room_number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    
    return abs(even_sum - odd_sum)

def calculate_diamonds(N):
    total_diamonds = 0
    
    for i in range(1, N + 1):
        room_number = i + (i % N) * N
        total_diamonds += get_even_odd_sum(room_number)
    
    return total_diamonds

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(calculate_diamonds(N))
