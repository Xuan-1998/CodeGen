t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    b.append(0)
    max_so_far = b[0]
    segment_sum = 0
    for i in range(n+1):
        if b[i] > max_so_far:
            if segment_sum != max_so_far**2:
                print("NO")
                break
            max_so_far = b[i]
            segment_sum = b[i]
        else:
            segment_sum += b[i]
    else:
        print("YES")

