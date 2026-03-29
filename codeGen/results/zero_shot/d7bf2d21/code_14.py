import sys

def find_lis(arr):
    dp = {x: 1 for x in arr}
    max_length = 0
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[arr[i]] = max(dp.get(arr[i], 0), dp.get(arr[j], 0) + 1)
                max_length = max(max_length, dp.get(arr[i], 0))
    
    count = 0
    for key, value in dp.items():
        if value == max_length:
            count += 1
    
    return count

arr = list(map(int, input().split()))
print(find_lis(arr))
