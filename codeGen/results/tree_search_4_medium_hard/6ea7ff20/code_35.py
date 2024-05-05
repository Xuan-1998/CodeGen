code:
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (2*n) for _ in range(2*n)]
    for i in range(n): 
        dp[i][i] = 1

    for length in range(2, 2*n+1):
        for left in range(2*n-length+1):
            right = left + length - 1
            if p[2*left-1] < p[2*right-1]:
                dp[left][right] = 1
                for i in range(left+length//2, right//2+1):
                    j = 2*i-right-1
                    k = 2*i-left-1
                    if dp[i][j] and dp[k][i]:
                        dp[left][right] = 0
                        break
            elif p[2*left-1] > p[2*right-1]:
                dp[left][right] = 0
    
    for i in range(2*n):
        if not dp[0][i]:
            print("NO")
            return
    print("YES")
