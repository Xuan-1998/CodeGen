t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    cum_sum = [0]
    for num in b:
        cum_sum.append(cum_sum[-1] + num)
    
    a = [0] * (n + 1)
    is_sendable = True
    
    for i in range(1, n + 1):
        if cum_sum[i] - cum_sum[i - 1] != i:
            is_sendable = False
            break
            
    if is_sendable:
        print("YES")
    else:
        print("NO")
