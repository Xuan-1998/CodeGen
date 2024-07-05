t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    max_so_far = b[0]
    total_sum = b[0]
    for i in range(1, n):
        total_sum += b[i]
        max_so_far = max(max_so_far, b[i])
        if total_sum < max_so_far * 2:
            print("NO")
            break
    else:
        if total_sum % 2 == 0 and total_sum // 2 >= max_so_far:
            print("YES")
        else:
            print("NO")

