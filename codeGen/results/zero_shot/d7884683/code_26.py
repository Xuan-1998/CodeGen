n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:len(arr)//2])
    right_sum = sum(arr[len(arr)//2:])
    count = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            left_sum -= arr[i]
        else:
            right_sum += arr[i]
        if left_sum == right_sum:
            count += 1
    print(count)
