t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    min_val, max_val = 1, b[0]
    for i in range(1, n):
        if b[i] > max_val or b[i] < min_val:
            print('NO')
            break
        else:
            if b[i] == max_val:
                min_val = max_val
                max_val = b[i+1] if i+1 < n else b[i]
            else:
                min_val = b[i]
                max_val = max_val
    else:
        print('YES')

