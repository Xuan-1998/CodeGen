t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    min_length = 1
    max_length = b[0]
    possible = True
    for i in range(1, n):
        if b[i] > max_length:
            possible = False
            break
        next_min_length = max(min_length, b[i])
        next_max_length = min(max_length, b[i-1]) + b[i] - next_min_length
        min_length, max_length = next_min_length, next_max_length
    print("YES" if possible else "NO")

