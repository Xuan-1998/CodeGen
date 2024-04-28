t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = 0
    count = 0
    for i in range(n):
        left_sum += arr[i]
        if left_sum == sum(arr[i+1:]):
            count += 1
            left_sum = 0
    print(count)
