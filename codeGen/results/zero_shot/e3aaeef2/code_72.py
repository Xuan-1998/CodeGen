import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    
    # Apply the operations
    for _ in range(m):
        n = str(n)
        n = ''.join(str(int(d) + 1) for d in n)
    
    # Find the length of the resulting number
    length = len(str(n))
    
    # Print the result modulo 10^9+7
    print(length % (10**9 + 7))
