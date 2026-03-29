t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    min_val = max_val = b[0]
    for i in range(1, n):
        if b[i] < min_val or b[i] > max_val:
            print("NO")
            break
        if b[i] > b[i - 1]:
            max_val = b[i]
            min_val = b[i - 1]
        else:
            min_val = b[i]
            max_val = b[i - 1]
    else:
        print("YES")

