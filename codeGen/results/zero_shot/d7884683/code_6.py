t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    max_count = 0
    for i in range(n//2+1):
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            count = 0
            left_sum, right_sum = sum(arr[:i]), sum(arr[i:])
            while left_sum == right_sum:
                left_sum -= arr[0]
                right_sum += arr[n-1]
                arr.pop(0)
                arr.pop()
                count += 1
            max_count = max(max_count, count+1)
    print(max_count)
