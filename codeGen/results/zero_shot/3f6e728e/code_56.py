import sys

def solve():
    T = int(input())
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        # Sort the radii of both upper and lower hemispheres
        U.sort()
        L.sort()
        
        dp = [0] * (C + 1)
        
        for i in range(N):
            for j in range(C, -1, -1):
                if j >= U[i]:
                    dp[j] += 1
        
        for i in range(M):
            for j in range(C, -1, -1):
                if j >= L[i]:
                    dp[j] += 1
        
        # Calculate the number of X-sequences
        ans = 0
        for i in range(C + 1):
            ans += (dp[i] * (C - i)) % (10**9 + 7)
        
        print(ans % (10**9 + 7))
