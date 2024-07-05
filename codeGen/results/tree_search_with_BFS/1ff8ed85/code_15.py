t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    min_val = max_val = b[0]
    possible = True
    for i in range(1, n):
        if b[i] < min_val - 1 or b[i] > max_val + 1:
            possible = False
            break
        min_val = min(min_val, b[i])
        max_val = max(max_val, b[i])
    print("YES" if possible else "NO")

