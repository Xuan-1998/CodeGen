# Take input for number of test cases
t = int(input())

for _ in range(t):
    # Take input for initial number n and operations m
    n, m = map(int, input().split())
    
    # Initialize length of number to 0
    len_n = 0
    
    # Apply operations m times
    for _ in range(m):
        # Increment length of number for each digit
        len_n += len(str(n))
        
        # Perform operation (replace each digit with d + 1)
        n = int(''.join(str(int(d) + 1) if d != '9' else '0' for d in str(n)))
    
    # Print length of resulting number modulo 10^9+7
    print(len_n % (10**9 + 7))
