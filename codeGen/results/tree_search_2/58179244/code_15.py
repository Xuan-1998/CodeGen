from collections import defaultdict

def min_recolor_lights(n, s):
    dp = defaultdict(lambda: defaultdict(bool))
    
    for i in range(n):
        if i == 0:
            dp[i][0] = True
        else:
            for p in range(i+1):
                diverse = False
                for j in range(3):
                    if (p > 0 and dp[i-1][p-1]) or (j == ord(s[i]) - ord('R')):
                        continue
                    diverse = True
                    break
                
                dp[i][p] = dp[i][p] or (diverse and dp[i-1][p])
                
    min_recolor = float('inf')
    res = ''
    
    for p in range(n+1):
        if dp[n][p]:
            min_recolor = min(min_recolor, p)
            res = s[:n-p] + 'RGB'[ord(s[n-p-1]) - ord('R')] * (p) + s[n-p:]
            
    print(min_recolor)
    print(res)

# Input
n = int(input())
s = input()

min_recolor_lights(n, s)
