def count_diamonds():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    # base case: only one room
                    even_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 == 0)
                    odd_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 != 0)
                    dp[i][j] = abs(even_sum - odd_sum)
                else:
                    # transition: calculate the number of diamonds based on previous rooms
                    even_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 == 0)
                    odd_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 != 0)
                    dp[i][j] = abs(even_sum - odd_sum) + dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1]
        
        print(dp[n][n])

count_diamonds()
