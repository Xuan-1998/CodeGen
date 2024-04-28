t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    left_sum = 0
    count = 0
    for i in range(n-1):
        left_sum += arr[i]
        if left_sum * 2 == total_sum:
            count += 1
        elif left_sum * 2 > total_sum:
            break
    print(count)
