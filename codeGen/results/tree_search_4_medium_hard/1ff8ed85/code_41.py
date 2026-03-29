from collections import deque

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [False] * (n + 1)
        even_odd = [False, False]
        
        for i in range(n):
            if b[i] % 2 == 0:
                even_odd[1] = True
            else:
                even_odd[0] = True
            
            for j in range(i+1):
                if even_odd[0]:
                    dp[j] = not dp[j]
                    even_odd[0] = False
                elif even_odd[1]:
                    dp[j] = not dp[j]
                    even_odd[1] = False
        
        print('YES' if dp[-1] else 'NO')

solve()
