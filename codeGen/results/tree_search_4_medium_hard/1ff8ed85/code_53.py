import sys

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = {}
        cum_sum = 0
        
        for i in range(n):
            if b[i] % 2 == 0:
                dp[cum_sum] = i
            cum_sum += b[i]
        
        for i in range(n-1, -1, -1):
            if i % 2 == 0:
                prev_even = -1
                cum_sum = 0
                
                for j in range(i, n, 2):
                    cum_sum += b[j]
                    
                    if j == n-1: break
                    if b[j] % 2 != 0:
                        prev_even = dp.get(cum_sum-b[j])
                        if prev_even != -1: break
                        
                if prev_even != -1:
                    print("YES")
                    return
                else:
                    print("NO")
            else:
                prev_odd = -1
                cum_sum = 0
                
                for j in range(i, n, 2):
                    cum_sum += b[j]
                    
                    if j == n-1: break
                    if b[j] % 2 == 0:
                        prev_odd = dp.get(cum_sum-b[j])
                        if prev_odd != -1: break
                        
                if prev_odd != -1:
                    print("YES")
                    return
                else:
                    print("NO")

if __name__ == "__main__":
    main()
