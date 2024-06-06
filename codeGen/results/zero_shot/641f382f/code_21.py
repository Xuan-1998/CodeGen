import math
import sys

# Step 1: Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Step 2: Check for direct solution
if 1 in arr:
    print(0)
else:
    # Step 3: Calculate GCDs
    operations = float('inf')
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i+1, n):
            current_gcd = math.gcd(current_gcd, arr[j])
            # Step 4: Find operations
            if current_gcd == 1:
                operations = min(operations, j - i)
                break
    # Step 5: Check for edge case
    if operations == float('inf'):
        print(-1)
    else:
        # We add (n-1) because we need to propagate the GCD = 1 to the entire array
        print(operations + (n - 1))
