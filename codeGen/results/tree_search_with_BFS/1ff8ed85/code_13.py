t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    left = right = b[0]
    for i in range(1, n):
        if not left <= b[i] <= right:
            print("NO")
            break
        left = max(left, b[i])
        if i != n-1:
            right = min(right, b[i] + b[i-1] - left)
    else:
        print("YES")

