from collections import defaultdict

def program_terminates(n, a):
    memo = {(1, 0): 0}
    
    for x in range(2, n+1):
        y = memo[(x-1, memo[(x-1, 0)]%x)]
        new_y = (y + a[x]) % x
        if new_y == 0:
            return -1
        memo[(x, y)] = new_y
    
    return memo[(n, 0)]

n = int(input())
a = list(map(int, input().split()))
for i in range(2, n+1):
    print(program_terminates(i, a))
