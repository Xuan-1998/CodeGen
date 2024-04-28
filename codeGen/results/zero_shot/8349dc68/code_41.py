n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_sum = 0
window_sum = 0
window_max = float('-inf')

for i in range(n):
    window_sum += arr[i]
    if i >= k:
        window_sum -= arr[i-k]
    
    if i >= k-1:
        window_max = max(window_max, window_sum)
        
    if i >= n - k:
        max_sum = max(max_sum, window_max * (k if i == n - k else 1))

print(max_sum)
