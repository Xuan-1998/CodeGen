def total_diamonds(n):
    total = 0
    for i in range(1, n+1):
        room_num = i + (i//10)%10
        even_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 != 0)
        total += abs(even_sum - odd_sum)
    return total

t = int(input())
for _ in range(t):
    n = int(input())
    print(total_diamonds(n))
