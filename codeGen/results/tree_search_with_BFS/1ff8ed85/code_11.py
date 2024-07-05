t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    if all(b[i] <= b[i+1] for i in range(n-1)):
        print('YES')
    else:
        print('NO')

