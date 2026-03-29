t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    minVal = maxVal = b[0]
    for i in range(1, n):
        if minVal > b[i] or maxVal < b[i]:
            print("NO")
            break
        else:
            maxVal = min(maxVal, b[i-1] + minVal - 1)
            minVal = max(minVal, b[i-1])
    else:
        print("YES")

