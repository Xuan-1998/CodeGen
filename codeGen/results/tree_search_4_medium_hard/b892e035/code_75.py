import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        
        dp = [[0] * (1 << 4) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            p1, num1, num2 = map(int, sys.stdin.readline().split())
            
            for state in range(1 << 4):
                if not ((state >> (num1 - 1)) & 1) and not ((state >> (num2 - 1)) & 1):
                    dp[i][state] = dp[i-1][state] * (p1 + p2)
                    
                elif state >> (num1 - 1) & 1:
                    if state >> (num2 - 1) & 1:
                        dp[i][state] = dp[i-1][state] * (1 - p1) * (1 - p2)
                    else:
                        dp[i][state] = dp[i-1][state] * (1 - p1)
                        
                elif state >> (num2 - 1) & 1:
                    if state >> (num1 - 1) & 1:
                        dp[i][state] = dp[i-1][state] * (1 - p2) * (1 - p1)
                    else:
                        dp[i][state] = dp[i-1][state] * (1 - p2)
                        
        print(format(dp[-1][-1], '.6f'))
