def sum_of_diamonds(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            num = i + j - 1
            even_sum = sum(int(digit) for digit in str(num) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(num) if int(digit) % 2 != 0)
            dp[i][j] = abs(even_sum - odd_sum)
    
    total_diamonds = sum(dp[-1])
    return total_diamonds

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum_of_diamonds(n))
