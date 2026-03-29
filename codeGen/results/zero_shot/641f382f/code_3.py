import math
import sys

def main():
    n = int(input().strip())
    array = list(map(int, input().strip().split()))

    # Check if there is an element that is already 1
    if 1 in array:
        print(0)
        return
    
    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    
    # Calculate the minimum number of operations required
    for i in range(n-1):
        gcd = math.gcd(array[i], array[i+1])
        operations = 0
        while gcd != 1:
            operations += 1
            # Move to the next pair
            if i + 1 + operations < n:
                gcd = math.gcd(gcd, array[i + 1 + operations])
            else:
                break
        if gcd == 1:
            min_operations = min(min_operations, operations)
            
    # If it is impossible to make all elements equal to 1
    if min_operations == float('inf'):
        print(-1)
    else:
        print(min_operations)

if __name__ == "__main__":
    main()
