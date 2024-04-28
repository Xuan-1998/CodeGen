code
n = int(input())
dp = {}
count = 0

for _ in range(n):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    left_sum = 0
    right_sum = total_sum
    
    for i in range(n):
        if left_sum == right_sum:
            count += 1
        left_sum += arr[i]
        right_sum -= arr[i]

print(count)
