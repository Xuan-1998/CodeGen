from math import gcd
from sys import stdin

def min_operations_to_make_ones(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0
    
    # Initialize the minimum number of operations to a large number
    min_operations = float('inf')
    
    # Compute the GCD of all adjacent pairs and check for 1
    for i in range(n - 1):
        current_gcd = gcd(arr[i], arr[i + 1])
        if current_gcd == 1:
            return 1  # We can make all elements equal to 1 in one operation
        
        # Find the shortest sequence of operations to get GCD of 1
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                min_operations = min(min_operations, j - i)
                break
    
    return min_operations if min_operations != float('inf') else -1

def main():
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    result = min_operations_to_make_ones(n, arr)
    print(result)

if __name__ == "__main__":
    main()
