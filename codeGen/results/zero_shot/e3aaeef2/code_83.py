import sys

def solve(n, m):
    # Count the number of digits in n
    num_digits = len(str(n))
    
    # Calculate the effective increment needed to reach the desired length
    effective_increment = (10 ** (num_digits - 1)) % (10**9 + 7)
    
    # Apply the operations
    while m >= effective_increment:
        m -= effective_increment
        num_digits += 1
    
    return num_digits % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
