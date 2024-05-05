    ===BEGIN CODE===
import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        prev_val = 0
        dp = {0: True}
        
        for i in range(n):
            if b[i] % prev_val != 0:
                print("NO")
                break
            prev_val = b[i]
        else:
            print("YES")

solve()
    ===END CODE===
