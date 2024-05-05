import math

def calculate_dp(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize base case
    for j in range(n + 1):
        dp[0][j] = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, n) + 1):
            for k in range(1, i + 1):
                if k > i - j:
                    break
                dp[i][j] += dp[k-1][j-1] * math.comb(i, k)
    
    return dp[n][n]

def main():
    n = int(input())
    m = list(map(int, input().split()))
    
    answer = calculate_dp(n)
    print(answer)

if __name__ == "__main__":
    main()
