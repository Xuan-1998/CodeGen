import sys

def main():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Initialize dp table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: When there are no more operations
        for i in range(1, n + 1):
            dp[0][i] = len(str(i))
        
        # Fill up the dp table using a bottom-up approach
        for k in range(1, m + 1):
            for i in range(1, n + 1):
                temp_len = dp[k - 1][i]
                new_num = 0
                carry = 0
                
                while i > 0:
                    d = (i % 10) + carry
                    if d >= 10:
                        d -= 9
                        carry = 1
                    else:
                        carry = 0
                    
                    i //= 10
                    new_num = new_num * 10 + d
                
                dp[k][new_num] = temp_len
                
        # Print the answer for each test case
        print(dp[m][n] % (10**9 + 7))

if __name__ == "__main__":
    main()
