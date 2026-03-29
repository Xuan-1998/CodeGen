import math

def solve():
    n = int(input())
    P = 1
    for i in range(1, n+1):
        P *= math.comb(n-1, i-1)
    print(P % 998244353)

if __name__ == "__main__":
    solve()
