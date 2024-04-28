n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    left_sum = 0
    right_sum = sum(arr)
    count = 1
    for i in range(len(arr)):
        if left_sum == right_sum:
            count += 1
            left_sum = 0
            right_sum = sum(arr[i+1:])
        elif left_sum < right_sum:
            left_sum += arr[i]
        else:
            right_sum -= arr[i]
    print(count)
