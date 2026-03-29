def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp1 = [[0] * (n + 1) for _ in range(10**6 + 7)]
    dp2 = [[0] * (n + 1) for _ in range(10**6 + 7)]
    
    for i in range(n):
        if a[i] % (i + 1):  # If the current element is not divisible by its position
            continue
        
        prefix_sum = sum(a[:i+1])
        dp2[prefix_sum][i+1] += 1
        
        if i:
            for j in range(prefix_sum):
                dp2[j][i+1] += dp2[j][i]
        
        for j in range(prefix_sum + 1):
            dp1[j][i+1] = (dp1[j][i] + dp2[j][i+1]) % (10**9 + 7)
    
    return sum(dp1[:]) % (10**9 + 7)

print(solve())
