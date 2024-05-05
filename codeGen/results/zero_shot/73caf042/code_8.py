def get_room_number(row, col):
    return row + col

def get_even_odd_digit_sums(room_number):
    even_sum = 0
    odd_sum = 0
    while room_number > 0:
        digit = room_number % 10
        if digit % 2 == 0:  # Even digit
            even_sum += digit
        else:  # Odd digit
            odd_sum += digit
        room_number //= 10
    return abs(even_sum - odd_sum)

def get_total_diamonds(N):
    total_diamonds = 0
    for row in range(1, N+1):
        for col in range(1, N+1):
            room_number = get_room_number(row, col)
            total_diamonds += get_even_odd_digit_sums(room_number)
    return total_diamonds

T = int(input())
for _ in range(T):
    N = int(input())
    print(get_total_diamonds(N))
