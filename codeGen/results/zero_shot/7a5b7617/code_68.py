import sys

def solve():
    T = int(sys.stdin.readline())
    MOD = 10 ** 9 + 7
    
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        total_sum = sum(range(N+1))
        if total_sum > M:
            print(0)
        else:
            res = 1
            for i in range(N-1):
                res *= (M - i) // (i + 1)
                res %= MOD
            print(res)

solve()
