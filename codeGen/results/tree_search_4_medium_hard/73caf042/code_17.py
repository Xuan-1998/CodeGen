def count_diamonds():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [[0] * n for _ in range(n)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                even_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(i+j-1) if int(digit) % 2 != 0)
                dp[i-1][j-1] = abs(even_sum - odd_sum)
        
        total_diamonds = sum(sum(row) for row in dp)
        print(total_diamonds)

count_diamonds()
