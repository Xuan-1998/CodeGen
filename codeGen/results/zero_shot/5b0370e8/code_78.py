python
# Step 1: Understand the problem statement and constraints
def count_bitwise_and_xor(t):
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Step 2: Calculate bitwise AND and XOR of all elements
        bitwise_and = arr[0]
        bitwise_xor = arr[0]
        for i in range(1, n):
            bitwise_and &= arr[i]
            bitwise_xor ^= arr[i]
            
        # Step 3: Count arrays that satisfy the condition
        count = 0
        for i in range(2**k):  # Iterate over all possible values of bitwise AND and XOR
            if (i & bitwise_and) >= bitwise_xor:
                count += 1
        
        print(count % (10**9 + 7))
