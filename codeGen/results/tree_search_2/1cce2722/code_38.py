def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + (1 if a[i] not in [a[j] - 1, a[j] + 1] for j in range(i)).count(True)
        
    print(max(dp))
