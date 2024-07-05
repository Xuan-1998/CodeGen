t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    minNum = 1
    maxNum = 1
    for i in range(n):
        if b[i] < minNum or b[i] > maxNum:
            print('NO')
            break
        minNum = max(minNum, b[i] + 1)
        maxNum = min(maxNum, b[i] + 1)
    else:
        print('YES')

