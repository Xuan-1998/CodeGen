def expectedCarries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N+1) for _ in range(N+1)]
        
        # Fill base case values
        for i in range(10):
            dp[i][i] = 0
        
        # Fill rest of array using state transition rules
        for length in range(2, N+1):
            for i in range(N-length+1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = (max(int(input()), int(input())) >= 10) * 1.0
                else:
                    carry = 0
                    for k in range(length-1):
                        if (int(input()) + int(input())) >= 10:
                            carry += 1
                        input()
                        input()
                    dp[i][j] = dp[i][j-1] + carry / (length-1.0)
        
        print(dp[0][N-1])

expectedCarries()
