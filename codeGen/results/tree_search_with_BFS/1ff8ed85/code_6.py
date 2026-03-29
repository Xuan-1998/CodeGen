t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    left = right = b[0]
    for i in range(1, n):
        if not left <= b[i] <= right:
            print('NO')
            break
        if i != n - 1:
            left = max(1, b[i] - min(b[i-1], b[i+1]))
            right = b[i] + min(b[i-1], b[i+1]) - 1
    else:
        print('YES')

