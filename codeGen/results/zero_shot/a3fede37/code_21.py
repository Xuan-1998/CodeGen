import sys

def solve():
    # Read the input
    n = int(sys.stdin.readline())
    tree = list(map(int, sys.stdin.readline().split()))
    
    # Initialize the maximum sum
    max_sum = float('-inf')
    
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if the node has a left child
        if left < n and tree[left] > 0:
            left_sum = tree[i] + tree[left]
            max_sum = max(max_sum, left_sum)
        
        # Check if the node has a right child
        if right < n and tree[right] > 0:
            right_sum = tree[i] + tree[right]
            max_sum = max(max_sum, right_sum)
    
    print(max_sum)

solve()
