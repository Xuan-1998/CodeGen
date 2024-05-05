code block:
memo = {}
def dp(x, y):
    if (x, y) in memo:
        return memo[(x, y)]
    
    if x <= 0 or x > n:
        result = -1
    else:
        new_x = x + a[x]
        new_y = y + a[x]
        new_x -= a[new_x]
        new_y += a[new_x]
        
        result = dp(new_x, new_y)
    
    memo[(x, y)] = result
    
    return result

n = int(input())  # read the length of the sequence
a = list(map(int, input().split()))  # read the sequence itself

result = 0
for i in range(2, n+1):
    x, y = dp(i-1, 0)
    if x <= 0 or x > n:
        result = -1
        break
    
print(result)
