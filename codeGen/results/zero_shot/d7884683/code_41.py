t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = 0
    right_sum = sum(arr)
    count = 0
    for i in range(n-1):
        right_sum -= arr[i]
        if left_sum == right_sum:
            count += 1
            left_sum = 0
            right_sum = sum(arr[:i+1])
    print(count)
