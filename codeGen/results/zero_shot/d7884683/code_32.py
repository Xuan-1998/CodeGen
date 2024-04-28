n = int(input())
sum_left = 0
max_partition = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    sum_right = sum(arr)
    while True:
        if sum_left == sum_right:
            max_partition += 1
            break
        elif sum_left < sum_right:
            sum_right -= arr[0]
            arr.pop(0)
        else:
            sum_left -= arr[-1]
            arr.pop()
