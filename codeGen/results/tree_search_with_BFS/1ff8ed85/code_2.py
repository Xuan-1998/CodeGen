t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    max1, max2 = b[0], 0
    for i in range(1, n):
        if b[i] > max2:
            max2, max1 = b[i], max2
        elif b[i] > max1:
            max2 = max(max2, b[i])
        else:
            print("NO")
            break
    else:
        print("YES")

