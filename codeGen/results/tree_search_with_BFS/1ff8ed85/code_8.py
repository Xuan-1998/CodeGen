t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    max_val = min_val = b[0]
    for i in range(1, n):
        if b[i] < min_val or b[i] > max_val + 1:
            print("NO")
            break
        max_val = max(max_val, b[i])
        min_val = min(min_val, b[i])
    else:
        print("YES")

