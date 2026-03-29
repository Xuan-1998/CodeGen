def even_odd_sum(room_number):
    odd_sum = 0
    even_sum = 0
    for digit in str(room_number):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return abs(even_sum - odd_sum)

T = int(input())  # read T from stdin

for _ in range(T):
    N = int(input())  # read N from stdin
    total_diamonds = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            room_number = i + j
            total_diamonds += even_odd_sum(room_number)
    print(total_diamonds)  # print the total number of diamonds
