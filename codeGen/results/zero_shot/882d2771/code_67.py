import sys

def solve():
    t, l, r = map(int, input().split())
    f = lambda x: (x + 1) ** 3 // 2
    result = sum(t * f(i) for i in range(l, r+1)) - l * f(r)
    print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
