import sys

def polygon_formation():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(3):
        if not moods[i]:
            break
    else:
        return "NO"
    
    for i in range(3, n + 1):
        if all(mood == 1 for mood in moods[:i]):
            dp[i] = dp[i - 1]
        else:
            dp[i] = False
    
    print("YES" if dp[n] else "NO")

polygon_formation()
