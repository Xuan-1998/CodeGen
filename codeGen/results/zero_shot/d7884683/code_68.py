t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = 0
    max_count = 0
    for i in range(n-1):
        left_sum += arr[i]
        right_sum = sum(arr[i+1:])
        if left_sum == right_sum:
            max_count += 1
            left_sum = 0
    print(max_count)
