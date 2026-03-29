def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = [0] + list(map(int, input().split()))
        l = []
        r = []
        for i in range(1, n+1):
            l.append(int(input()))
            r.append(int(input()))
        ans = 0
        for i in range(2, n+1):
            diff = l[i] - r[p[i]]
            if diff > 0:
                ans += diff
        print(ans)

solve()
