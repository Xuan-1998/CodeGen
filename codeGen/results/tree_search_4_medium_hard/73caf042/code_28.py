def calculate_diamonds():
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            room_number = i + j
            even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
            odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
            
            dp[i][j] = abs(even_sum - odd_sum)
    
    total_diamonds = sum(sum(row) for row in dp[1:])
    print(total_diamonds)

calculate_diamonds()
