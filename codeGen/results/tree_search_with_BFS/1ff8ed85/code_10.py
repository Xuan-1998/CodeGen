t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    min_possible, max_possible = 1, b[0]
    for i in range(1, n):
        if b[i] < min_possible or b[i] > max_possible:
            print("NO")
            break
        min_possible, max_possible = max(b[i], min_possible - b[i-1]), min(b[i], max_possible + b[i-1])
    else:
        print("YES")

