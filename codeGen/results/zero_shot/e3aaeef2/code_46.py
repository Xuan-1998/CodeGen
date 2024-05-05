# Read the input
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    # Apply the operations
    while m > 0:
        if '4' not in str(n) and '7' not in str(n):
            break
        n += 1
        m -= 1
    
    # Print the length of the resulting number modulo 10^9+7
    print(len(str(n)) % (10**9 + 7))
