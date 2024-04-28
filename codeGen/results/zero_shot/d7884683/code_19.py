t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    right_sum = sum(arr[n//2:])
    count = 0
    for i in range(n-1):
        if (left_sum + arr[i+1]) == right_sum:
            count += 1
            left_sum += arr[i+1]
            right_sum -= arr[i+1]
        else:
            break
    print(count)
