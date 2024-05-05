def total_diamonds(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            room_num = i + j
            even_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(room_num) if int(digit) % 2 != 0)
            dp[i][j] = abs(even_sum - odd_sum)
    
    total_diamonds = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            total_diamonds += dp[i][j]
    
    return total_diamonds

T = int(input())
for _ in range(T):
    N = int(input())
    print(total_diamonds(N))
