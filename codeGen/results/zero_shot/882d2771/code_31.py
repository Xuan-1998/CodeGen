import sys

def solve():
    t, l, r = map(int, input().split())
    
    # Calculate f(n) for each n in range(l, r+1)
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        dp[i] = min((dp[j] + j - i) % (10**9 + 7) for j in range(i))
    
    # Calculate the expression
    res = sum(t * (dp[l + i] + l - (l + i)) % (10**9 + 7) for i in range(r - l + 1))
    
    print(res % (10**9 + 7))

if __name__ == "__main__":
    solve()
