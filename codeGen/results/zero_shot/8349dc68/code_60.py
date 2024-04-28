n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_sum = 0
i = 0
while i < n:
    window_sum = sum(arr[i:i+k])
    max_sum = max(max_sum, window_sum)
    i += k
print(max_sum)
