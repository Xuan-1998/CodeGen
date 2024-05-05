def infinite_zoo():
    q = int(input())
    
    dp = [False] * (2**30)
    dp[0] = True
    
    for i in range(2**30):
        if not dp[i]:
            continue
        for j in range(i.bit_length()):
            new_bit = i & ~(1 << j)
            if not dp[new_bit]:
                dp[new_bit] = True
    
    result = []
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        while v:
            if not (u & 1) and dp[v^1]:
                u ^= 1
            else:
                break
            v >>= 1
        
        result.append("YES" if v == 0 else "NO")
    
    print("\n".join(result))

infinite_zoo()
