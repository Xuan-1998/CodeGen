def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize table with -1 values
    table = [[-1] * (10**9 + 1) for _ in range(n+1)]
    
    for i in range(2, n+1):
        x, y = 1, 0
        while True:
            if a[x-2] > 10**9 or x <= 0 or x > n:
                break
            x += a[x-2]
            y += a[x-2]
            table[i][y] = min(table[i][y], y)
    
    print(table[n-1][0])

solve()
