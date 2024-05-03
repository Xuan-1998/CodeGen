from math import exp

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [0] * (1 << n)
        res = 0
        for i in range(n):
            p1, n1, n2 = map(int, input().split())
            s = set()
            if p1 > 0:
                s.add(0)
            if p2 > 0:
                s.add(1)
            for j in range(i + 1):
                res += dp[j] * exp((p1 if i == j else 0) + (p2 if i != j else 0))
        print(exp(res))

if __name__ == "__main__":
    solve()
