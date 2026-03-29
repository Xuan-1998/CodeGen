import sys

def solve():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True  # base case: one knight is always regular
    
    for i in range(1, n + 1):
        if moods[i-1]:  # good mood
            if (i+1) % (i+1) == 0:  # check if number of good knights is a multiple of (n+1)
                dp[i] = True
            else:
                dp[i] = dp[i-1]
        else:  # bad mood
            dp[i] = False
    
    print("YES" if dp[n] else "NO")

if __name__ == "__main__":
    solve()
