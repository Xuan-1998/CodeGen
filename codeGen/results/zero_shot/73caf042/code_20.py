def sum_even_odd_digits(n):
    even_sum = 0
    odd_sum = 0
    while n:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        n //= 10
    return abs(even_sum - odd_sum)

def calculate_diamonds(n):
    total_diamonds = 0
    for i in range(1, n+1):
        room_number = (i + i) // 2
        total_diamonds += sum_even_odd_digits(room_number)
    return total_diamonds

t = int(input())
for _ in range(t):
    n = int(input())
    print(calculate_diamonds(n))
