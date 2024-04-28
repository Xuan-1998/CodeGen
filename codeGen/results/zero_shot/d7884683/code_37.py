t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    count = 1
    for i in range(n//2, n):
        if sum(arr[i:]) == left_sum:
            count += 1
        else:
            break
    print(count)
