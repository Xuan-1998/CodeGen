import sys

def solve(n, M):
    MOD = 10**9 + 7
    
    # Initialize dp array with base case values
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        prev_max = -1
        ways = 0
        
        for j in range(i):
            if M[j] > prev_max:
                prev_max = M[j]
                # Calculate the number of different ways to create a collection V with one fewer element
                ways += dp[j]
                ways %= MOD
                
        dp[i] = ways
    
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    M = list(map(int, input().split()))
    
    result = solve(n, M)
    print(result)
