import sys

def longest_increasing_subsequence():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    
    max_length = 0
    last_index = -1
    
    for i in range(n):
        if dp[i] > max_length:
            max_length = dp[i]
            last_index = i
            
    sequence = []
    while last_index != -1:
        sequence.append(arr[last_index])
        last_index = prev[last_index]
        
    print(max_length)
    print(*sequence[::-1], sep='\n')

longest_increasing_subsequence()
