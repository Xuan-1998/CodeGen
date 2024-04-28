t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    count = 0
    for i in range(n//2+1, n+1):
        if sum(arr[:i]) == left_sum:
            count += 1
    print(count)
