import math

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = 1
        for i in range(N):
            result *= math.comb(M - sum(range(i+1)), N-i)
        print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
