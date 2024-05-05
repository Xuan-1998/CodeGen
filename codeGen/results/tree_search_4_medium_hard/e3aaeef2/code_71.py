def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        res = 0
        while m > 0:
            if n >= 10 ** (res + 1):
                res += 1
            else:
                break
            m -= res
        print(res % (10**9 + 7))

if __name__ == "__main__":
    solve()
