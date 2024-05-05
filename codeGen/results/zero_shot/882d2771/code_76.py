import sys
input = sys.stdin.readline

def solve():
    t, l, r = map(int, input().split())
    
    # Calculate f(n) using dynamic programming
    dp = [0] * (r - l + 1)
    for i in range(2, r - l + 1):
        dp[i-1] = min((dp[j-1] if j > 0 else 0) + 1 for j in range(i))
    
    # Calculate the expression
    result = sum(t * (dp[j-l+1] if j >= l else 0) for j in range(l, r+1)) - l * dp[r-l]
    print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
