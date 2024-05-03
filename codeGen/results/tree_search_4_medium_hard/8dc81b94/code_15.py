def make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    memo = {0: True}
    
    for i in range(1, n+1):
        memo[i-1] = False
        
        if i == 1:
            memo[0] = (arr[0] == 0)
        else:
            for j in range(min(arr), max(arr)+1):
                if j <= 0 and memo.get(j-1, False):
                    return "YES"
                elif j >= 0 and memo.get(i-j-1, False):
                    return "YES"
        
        memo[i-1] = True
    
    return "NO"

print(make_zero())
