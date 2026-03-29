# Read input
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    # Convert number to string for easier manipulation
    num_str = str(n)
    
    # Apply operations
    for _ in range(m):
        new_num_str = ''
        for d in num_str:
            new_num_str += str(int(d) + 1)
        num_str = new_num_str
    
    # Calculate length of resulting number modulo 10^9+7
    length = len(num_str)
    
    print(length % (10**9 + 7))
