import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        dp = [[0]*(2**k) for _ in range(k+1)]
        dp[0][0] = 1
        
        for num in arr:
            i = k
            while i >= 0 and not (num & (1<<i)):
                i -= 1
            
            if i >= 0:
                j = num & ((1<<i)-1)
                for x in range(2**k):
                    dp[i][x] += dp[i-1][(x^(j<<(k-i)))]
        
        res = sum(dp[-1])
        print(res%10**9+7)

if __name__ == "__main__":
    solve()
