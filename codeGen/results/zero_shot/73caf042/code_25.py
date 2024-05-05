import sys

def even_odd_digits(n):
    even_digits = [int(d) for d in str(n) if int(d) % 2 == 0]
    odd_digits = [int(d) for d in str(n) if int(d) % 2 != 0]
    return even_digits, odd_digits

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_diamonds = 0
    for i in range(N):
        for j in range(N):
            room_number = (i + 1) * (j + 1)
            even_digits, odd_digits = even_odd_digits(room_number)
            diamonds = abs(sum(even_digits) - sum(odd_digits))
            total_diamonds += diamonds
    print(total_diamonds)
