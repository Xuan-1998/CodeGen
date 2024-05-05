def calculate_diamonds_per_room(room_number):
    even_sum = 0
    odd_sum = 0
    for digit in str(room_number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return abs(even_sum - odd_sum)

def calculate_total_diamonds(n):
    total_diamonds = 0
    for i in range(1, n+1):
        room_number = i + (i-1)
        diamonds_per_room = calculate_diamonds_per_room(room_number)
        total_diamonds += diamonds_per_room * n
    return total_diamonds

T = int(input())  # read the number of test cases
for _ in range(T):
    N = int(input())  # read the size of the grid for each test case
    print(calculate_total_diamonds(N))  # calculate and print the total number of diamonds
