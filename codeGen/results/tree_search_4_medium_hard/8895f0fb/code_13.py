def expectedCarries():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        # Create a 2D DP table to store the number of non-zero carries for each pair of digits in A and B.
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        # Fill the base case when i or j is equal to N, indicating that we are considering the last digit of either A or B.
        for i in range(N + 1):
            dp[i][N] = 0
            dp[N][i] = 0
        
        # Iterate over each pair of digits (i, j) in A and B, starting from the most significant digit to the least significant digit.
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if sum([int(x) for x in str(i)] + [int(x) for x in str(j)]) <= 9:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
        
        # Calculate the expected number of non-zero carries by summing up the values in the DP table and dividing by the total number of pairs.
        totalCarries = sum([sum(row) for row in dp])
        
        print(totalCarries / (N ** 2))

expectedCarries()
