def calculate_room_numbers(n):
    room_numbers = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            room_number = i + j
            room_numbers.append(room_number)
    return room_numbers

def calculate_diamonds(room_numbers):
    diamonds = []
    for room_number in room_numbers:
        even_digits_sum = 0
        odd_digits_sum = 0
        for digit in str(room_number):
            if int(digit) % 2 == 0:  # even digit
                even_digits_sum += int(digit)
            else:  # odd digit
                odd_digits_sum += int(digit)
        diamond_count = abs(even_digits_sum - odd_digits_sum)
        diamonds.append(diamond_count)
    return diamonds

n = int(input())  # input N from stdin
room_numbers = calculate_room_numbers(n)

diamonds = calculate_diamonds(room_numbers)

total_diamonds = sum(diamonds)

print("Total diamonds:", total_diamonds)  # print the total number of diamonds
