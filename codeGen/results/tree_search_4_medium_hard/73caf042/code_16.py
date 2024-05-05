def calculate_diamonds(N):
    dp = [[0] * N for _ in range(N)]
    memo = {}
    
    def sum_even_odd(room_num):
        even_sum = 0
        odd_sum = 0
        
        for digit in str(room_num):
            if int(digit) % 2 == 0:
                even_sum += int(digit)
            else:
                odd_sum += int(digit)
        
        return abs(even_sum - odd_sum)
    
    def dp_calculate(i, j):
        if i > 0 and j > 0:
            room_num = (i + j) // 2
            if room_num not in memo:
                memo[room_num] = sum_even_odd(room_num)
            return dp[i-1][j-1] + memo[room_num]
        elif i > 0:
            return dp[i-1][j]
        elif j > 0:
            return dp[i][j-1]
        else:
            room_num = (i + j) // 2
            if room_num not in memo:
                memo[room_num] = sum_even_odd(room_num)
            return memo[room_num]
    
    for i in range(N):
        for j in range(N):
            dp[i][j] = dp_calculate(i, j)
    
    return dp[N-1][N-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(calculate_diamonds(N))
