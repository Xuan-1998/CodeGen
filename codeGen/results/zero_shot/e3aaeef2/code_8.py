import sys

def solve(n, m):
    # Initialize the result length to 1 (since we start with a single-digit number)
    res_len = 1
    
    while True:
        # Apply one operation to n
        new_n = int(''.join(map(str, [int(digit) + 1 for digit in str(n)])))
        
        # Check if the operation changed the length of the number
        if len(str(new_n)) != res_len:
            res_len += 1
        
        # If we've applied m operations, break out of the loop
        if m == 0:
            break
        
        # Decrement the remaining operations counter
        m -= 1
        
        # Update n for the next iteration
        n = new_n
    
    return len(str(n)) % (10**9 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
