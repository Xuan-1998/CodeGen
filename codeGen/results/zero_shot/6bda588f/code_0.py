n = int(input())
for _ in range(n):
    s, *arr = map(int, input().split())
    arr.sort()
    min_val = float('inf')
    for i in range(len(arr)-1):
        x, y = (s + arr[i]), (2*s + arr[i+1] - arr[i])
        F = x*y
        if F < min_val:
            min_val = F
    print(min_val)
