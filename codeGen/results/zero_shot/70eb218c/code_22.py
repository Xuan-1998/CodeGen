def min_operations(n, x):
    curr_len = len(str(x))
    
    if curr_len == n:
        return 0
    
    ops = 0
    while curr_len < n:
        for y in range(2, 10):
            if (x * y) >= 10**(n-1):  # Check if multiplying by y would exceed the limit
                continue
            next_x = x * y
            next_len = len(str(next_x))
            if next_len == n:
                return ops + 1
            ops += 1
            x = next_x
            curr_len = next_len
    
    return -1

n, x = map(int, input().split())
print(min_operations(n, x))
