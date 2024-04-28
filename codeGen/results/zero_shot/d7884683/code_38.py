t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    right_sum = sum(arr[n//2:])
    count = 0
    for i in range(n-1):
        if sum(arr[:i+1]) == sum(arr[i+1:]):
            count += 1
            arr.pop(i)
            if len(arr) > 0:
                left_sum = sum(arr[:len(arr)//2])
                right_sum = sum(arr[len(arr)//2:])
            else:
                break
    print(count + 1)
