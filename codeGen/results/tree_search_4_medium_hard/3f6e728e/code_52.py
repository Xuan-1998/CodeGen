import sys
from math import comb

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = {0: 1}
        for i in range(1, C+1):
            dp[i] = (i-1) * dp.get(i-1, 0) + sum((k+1)**(C-k) * comb(C-i, k) for k in range(max(0, i-C+1)))

        print(*[dp[i] % (10**9 + 7) for i in range(C)], sep=' ')

if __name__ == '__main__':
    solve()
