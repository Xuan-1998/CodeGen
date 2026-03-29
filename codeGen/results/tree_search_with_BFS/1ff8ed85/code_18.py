t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    min_val, max_val = b[0], b[0]
    for i in range(1, n):
        if b[i] < min_val or b[i] > max_val:
            print("NO")
            break
        min_val = min(b[i], max_val - b[i-1])
        max_val = max(b[i], max_val - b[i-1])
    else:
        print("YES")

