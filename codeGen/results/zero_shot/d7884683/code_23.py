t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    right_sum = sum(arr[n//2:])
    count = 0
    for i in range(n//2):
        if sum(arr[i:i+n//2]) == left_sum:
            count += 1
            left_sum -= arr[i]
            right_sum += arr[i]
    print(count)
