import sys

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        prefix_sum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
            
        for i in range(1, n + 1):
            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] == 0:
                    dp[i][j] = True
                else:
                    for k in range(j + 1, i):
                        if prefix_sum[k] - (prefix_sum[i] - prefix_sum[k]) == 0 and dp[k][j]:
                            dp[i][j] = True
                            break
                
        count = 0
        left = n
        
        while left > 0:
            for right in range(left, -1, -1):
                if dp[left][right]:
                    count += 1
                    left = right
                    break
        print(count)

if __name__ == "__main__":
    main()
