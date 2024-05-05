import sys

def solve():
    n = int(sys.stdin.readline().strip())
    M = list(map(int, sys.stdin.readline().split()))
    
    # Initialize dp table with zeros
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(i+1):
            if M[j-1] < M[i]:
                dp[i+1] += dp[j]
                dp[i+1] %= 10**9 + 7
            else:
                break
    
    return dp[-1]

if __name__ == "__main__":
    print(solve())
