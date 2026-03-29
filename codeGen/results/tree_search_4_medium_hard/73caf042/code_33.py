def calculate_digits(n):
    even_sum = 0
    odd_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        n //= 10
    return even_sum, odd_sum

def calculate_diamonds(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            even_sum, odd_sum = calculate_digits(i * n + j)
            dp[i][j] = abs(even_sum - odd_sum)
    return sum(sum(row) for row in dp)

T = int(input())
for _ in range(T):
    N = int(input())
    print(calculate_diamonds(N))
