def can_send(b):
    n = len(b)
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        result = False
        for k in range(j+1):
            if b[i] <= k and dp(i-1, k):
                result = True
                break
        memo[(i, j)] = result
        return result
    
    for i in range(1, n+1):
        for j in range(1, min(i+1, 2*n)+1):
            if b[i-1] <= j and not dp(i-1, j-1):
                memo[(i, j)] = False
            else:
                result = False
                for k in range(j+1):
                    if b[i] <= k and dp(i-1, k):
                        result = True
                        break
                if not result:
                    return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_send(b) else "NO")
