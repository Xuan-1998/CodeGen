def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        ans = float('inf')
        for i in range(n):
            x = (a[i] + s) // 2
            y = a[i] - x
            f = a[0] * x + y * a[1]
            for j in range(2, n):
                f += (x - s) * (y - s)
                x = (a[j] + s) // 2
                y = a[j] - x
            ans = min(ans, f)
        print(ans)

if __name__ == '__main__':
    solve()
