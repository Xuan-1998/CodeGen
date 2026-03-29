def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print((m % (len(str(n)) - 1 + 1)) % (10**9 + 7))

solve()
