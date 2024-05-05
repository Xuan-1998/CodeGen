import sys
def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        # Step 1: Sort the array A.
        a.sort()
        
        # Step 2: Calculate the prefix XOR of the array A.
        prefix_xor = [0]
        for i in range(n):
            prefix_xor.append(prefix_xor[-1] ^ a[i])
        
        # Step 3: Initialize two variables, one to keep track of the maximum sum and another to keep track of whether we need to add X to any element or not.
        max_sum = 0
        add_x = False
        
        # Step 4: Iterate over the prefix XOR array from left to right.
        for i in range(1, n+1):
            # If the current element is greater than or equal to X and we haven't added X to any element yet, then update max_sum accordingly.
            if a[i-1] >= X and not add_x:
                max_sum = max(max_sum, prefix_xor[i] - prefix_xor[0])
                add_x = True
            # If the current element is less than X and we have already added X to any element, then update max_sum accordingly.
            elif a[i-1] < X and add_x:
                max_sum = max(max_sum, prefix_xor[i] - prefix_xor[0])
        
        print(max_sum)

if __name__ == "__main__":
    solve()
