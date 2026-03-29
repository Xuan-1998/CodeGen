import sys

def solve():
    t, l, r = map(int, input().split())
    mod = 10**9 + 7
    result = (t0 := t * pow(l-1, -1, mod)) % mod
    for i in range(1, r+1):
        result += (ti := ti + t) * (pow(i, -1, mod))
    print(result)

if __name__ == "__main__":
    solve()
