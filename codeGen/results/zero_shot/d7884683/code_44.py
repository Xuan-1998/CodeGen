t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    left_sum = 0
    count = 0
    for i in range(n):
        left_sum += arr[i]
        if left_sum == (total_sum - left_sum) // 2:
            count += 1
    print(count)
