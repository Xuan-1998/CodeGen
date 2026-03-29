from math import gcd
from sys import stdin

# Function to read input and solve the problem
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Calculate the GCD of the entire array
    array_gcd = arr[0]
    for num in arr[1:]:
        array_gcd = gcd(array_gcd, num)

    # If the GCD of the entire array is not 1, it's impossible to make all elements 1
    if array_gcd != 1:
        print(-1)
        return

    # If there is already a '1' in the array, no operations are needed
    if 1 in arr:
        print(0)
        return

    # Find the minimum number of operations required
    operations = 0
    for i in range(n):
        current_gcd = arr[i]
        # If the current element is 1, continue
        if current_gcd == 1:
            continue
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            # Once we find a GCD of 1, we add the distance to the operations
            if current_gcd == 1:
                operations += j - i
                break

    print(operations)

# Read from stdin and solve the problem
if __name__ == "__main__":
    solve()
