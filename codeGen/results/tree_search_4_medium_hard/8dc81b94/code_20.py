def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    memo = {}
    
    def dp(i):
        if i in memo:
            return memo[i]
        
        total_sum = sum(arr[:i+1])
        
        if total_sum == 0 or (total_sum < 0 and any(x > 0 for x in arr[:i])) or (total_sum > 0 and all(x <= 0 for x in arr[:i])):
            return True
        
        memo[i] = False
        for j in range(i+1):
            if not dp(j) or not dp(i-j-1):
                memo[i] = True
                break
        return memo[i]
    
    print("YES" if dp(n-1) else "NO")

if __name__ == "__main__":
    can_make_zero()
