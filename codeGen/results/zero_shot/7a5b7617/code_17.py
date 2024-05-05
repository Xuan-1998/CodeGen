import sys

def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        res = 0
        if n == 1:
            res = 1
        else:
            for i in range(m+1):
                if i < m//n:
                    res += 1
                elif i == m//n and m % n > 0:
                    res += (m//n) * (n-1) + 1
                else:
                    break
        print(res % int(10**9+7))

if __name__ == "__main__":
    solve()
