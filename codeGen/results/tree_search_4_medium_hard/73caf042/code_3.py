def total_diamonds(N):
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            room_number = i + j - 1
            even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            dp[i][j] = dp[i-1][j] + abs(even_sum - odd_sum) - (dp[i-1][j-1] if j > 0 else 0)
    
    return sum(sum(row) for row in dp)

T = int(input())
for _ in range(T):
    N = int(input())
    print(total_diamonds(N))
