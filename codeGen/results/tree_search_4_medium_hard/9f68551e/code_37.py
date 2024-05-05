import sys

def solve():
    n = int(input())
    dp = {}
    
    for i in range(n):
        k_i, h_i = map(int, input().split())
        
        for j in range(k_i+1):
            if (i, j) not in dp:
                if i == 0:
                    dp[(i, j)] = max(0, j)
                else:
                    if k_i <= j:
                        dp[(i, j)] = min(dp.get((i-1, max(0, j-k_i))), h_i) + (j > k_i)
                    else:
                        dp[(i, j)] = sys.maxsize
            print(dp[(i, j)], end=' ')
        print()

solve()
