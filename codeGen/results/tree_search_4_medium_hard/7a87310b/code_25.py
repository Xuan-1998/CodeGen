import sys

def solve():
    T = int(sys.stdin.readline())
    N = [int(_) for _ in sys.stdin.read().split()][:T]
    
    dp = [0] * (N[-1]+1)
    dp[1] = 1
    
    for i in range(2, N[-1]+1):
        for j in range(i):
            if (i-j) % 2 == 1:  # only consider odd traces
                dp[i] += dp[j] * ((i-j)//2+1)
    
    return '\n'.join(str(dp[n]) for n in N)

print(solve())
