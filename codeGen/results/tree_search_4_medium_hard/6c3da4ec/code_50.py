import sys

def solve():
    n = int(input())
    s = input()
    
    dp = {}
    for i in range(n):
        for j in range(i+1, n):
            dp[(i, j)] = 0
            for k in range(i, j):
                if not (k in [m for m in range(i) if dp.get((m, k), 0) == 1]):
                    dp[(i, j)] = max(dp.get((i, k), 0), dp.get((k, j), 0)) | int(s[k]) & (1 << (s[k] - '0'))
    
    print(max(str(bin(x))[2:].zfill(n) for x in range(2**len(s))))

solve()
