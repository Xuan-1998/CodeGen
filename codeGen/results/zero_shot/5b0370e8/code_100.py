python
def count_and_greater_than_xor(n, k):
    total_xor = 0
    total_and = 0
    
    for i in range(n):
        # Calculate XOR of all elements so far
        total_xor ^= int(input())
        
        # Calculate AND of all elements so far
        total_and &= int(input())
        
    return ((2**k-1) | total_and) > total_xor

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    count = 0
    
    for i in range(n):
        if count_and_greater_than_xor(n, k):
            count += 1
            
    print(count % (10**9 + 7))
