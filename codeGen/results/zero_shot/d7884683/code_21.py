t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = 0
    right_sum = sum(arr)
    count = 1
    for i in range(n-1):
        left_sum += arr[i]
        right_sum -= arr[i]
        if left_sum == right_sum:
            count += 1
    print(count)
