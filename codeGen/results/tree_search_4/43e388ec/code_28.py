import sys

def solve():
    a, b = map(int, input().split())
    
    dp = {}
    
    for i in range(a):
        for j in range(b):
            if i == 0:
                dp[(i, j)] = 0
            elif (i-1, j) not in dp:
                dp[(i, j)] = dp.get((i-1, j), 0)
            else:
                dp[(i, j)] = (dp[(i-1, j)] + (dp.get((i-1, j-1), 0) if j > 0 else 0)) % (10**9+7)

    print(dp.get((a-1, b-1), 0))

if __name__ == "__main__":
    solve()
