def count_diamonds():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i > 1 and j > 1:
                    room_number = i + j - 1
                    even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
                    odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
                    dp[i][j] = abs(even_sum - odd_sum) + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
        
        print(dp[n][n])

count_diamonds()
