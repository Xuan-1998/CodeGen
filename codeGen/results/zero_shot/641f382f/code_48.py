import math
from sys import stdin

def main():
    # Read the input
    n = int(stdin.readline().strip())
    array = list(map(int, stdin.readline().strip().split()))

    # Check if it's possible to make all elements equal to 1
    overall_gcd = array[0]
    for num in array:
        overall_gcd = math.gcd(overall_gcd, num)
    
    if overall_gcd > 1:
        print(-1)
        return

    # Find the minimum number of operations
    min_operations = 0
    for i in range(n):
        gcd = array[i]
        operations = 0
        # Iterate through the array to find the number of operations to make array[i] = 1
        for j in range(i+1, n):
            gcd = math.gcd(gcd, array[j])
            operations += 1
            if gcd == 1:
                min_operations += operations
                break

    print(min_operations)

if __name__ == "__main__":
    main()
