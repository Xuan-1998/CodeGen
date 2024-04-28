import sys

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [0] * (n + 1)
        
        total_sum = sum(arr)
        
        for i in range(1, n + 1):
            if i % 2 == 1:
                left_sum = total_sum - sum(arr[:i])
                right_sum = sum(arr[i:])
                
                if left_sum % 2 == 0 and right_sum % 2 == 0:
                    dp[i] = max(dp[i-1], dp[i//2-1]+1)
            else:
                dp[i] = max(dp[i-1], 0)
        
        print(max(dp))

if __name__ == "__main__":
    solve()
