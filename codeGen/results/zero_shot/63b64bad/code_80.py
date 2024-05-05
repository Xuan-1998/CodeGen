def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    for x in range(1, n+1):
        y = 0
        while True:
            x += a[x]
            if x > n or x <= 0:
                break
            y += a[x]
            x -= a[x]
        print(y)

solve()
