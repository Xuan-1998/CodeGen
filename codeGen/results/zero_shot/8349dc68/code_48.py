n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_sum = 0
for i in range(0, n, k):
    window_sum = sum(arr[i:i+k])
    max_sum = max(max_sum, window_sum)
    
print(max_sum)
