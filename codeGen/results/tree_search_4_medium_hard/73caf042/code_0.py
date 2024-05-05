def count_diamonds():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                room_number = i + j
                even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
                odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
                dp[i][j] = abs(even_sum - odd_sum)
        
        total_diamonds = sum(dp[i][j] for i in range(1, N + 1) for j in range(1, N + 1))
        print(total_diamonds)

count_diamonds()
