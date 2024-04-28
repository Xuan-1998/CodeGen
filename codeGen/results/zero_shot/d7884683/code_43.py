t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = 0
    max_count = 0
    for i in range(n):
        left_sum += arr[i]
        if left_sum == sum(arr[i+1:]):
            max_count += 1
            left_sum = 0
    print(max_count)
