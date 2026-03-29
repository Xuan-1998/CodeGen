t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    max_seen = min_seen = b[0]
    for i in range(1, n):
        if b[i] > max_seen:
            max_seen = b[i]
        if b[i] < min_seen:
            min_seen = b[i]
        if b[i] < min_seen or b[i] > max_seen:
            print('NO')
            break
    else:
        print('YES')

