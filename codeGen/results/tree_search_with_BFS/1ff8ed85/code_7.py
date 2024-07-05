t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    left, right = 0, n - 1
    maxLeft, maxRight = b[left], b[right]
    while left < right:
        if b[left] > maxLeft:
            maxLeft = b[left]
        if b[right] > maxRight:
            maxRight = b[right]
        if maxLeft > b[right] or maxRight > b[left]:
            print("NO")
            break
        left += 1
        right -= 1
    else:
        print("YES")

