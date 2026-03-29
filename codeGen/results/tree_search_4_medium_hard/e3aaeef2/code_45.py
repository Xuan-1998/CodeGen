import sys

def main():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Create a 2D array dp where dp[i][j] represents the length of the resulting number after applying j operations, given that the initial number has i digits.
        dp = [[0] * (m + 1) for _ in range(11)]
        
        # Base case: if there are no digits initially, then the length is always 1
        for j in range(m + 1):
            dp[0][j] = 1
        
        # Fill up the dp array using a bottom-up approach
        for i in range(1, n + 1):
            for j in range(min(i, m) + 1):
                # The maximum possible number of digits that can be obtained by applying j operations to an i-digit number is ceil(i / 2)
                dp[i][j] = min(dp[i - 1][j], ceil(i / 2))
        
        # Print the length of the resulting number after applying m operations, given that the initial number has n digits
        print((dp[n][m]) % (10 ** 9 + 7))

if __name__ == "__main__":
    main()
