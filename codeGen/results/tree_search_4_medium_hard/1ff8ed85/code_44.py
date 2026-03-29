import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    b = list(map(int, sys.stdin.readline().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        even = odd = False
        j = 0
        while j < i:
            if b[j % n] % 2 == 0: 
                even = True; 
            else: 
                odd = True
            if (even and not odd) or (not even and odd): 
                dp[i] = True; break
            j += 1
    
    print("YES" if any(dp[i]) for i in range(n + 1)) else print("NO")
