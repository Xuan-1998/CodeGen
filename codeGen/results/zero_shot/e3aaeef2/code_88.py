import sys
input = sys.stdin.readline

def calculate_length(n, m):
    # Calculate the length of the number after applying m operations
    length_after_operations = 0
    while n > 0:
        length_after_operations += 1
        n //= 10
    
    # Apply m operations and update the length
    for _ in range(m):
        temp = 0
        while n > 0:
            digit = n % 10
            temp = temp * 10 + (digit + 1)
            n //= 10
        
        length_after_operations += len(str(temp))
        n = temp
    
    return length_after_operations % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(calculate_length(n, m))
