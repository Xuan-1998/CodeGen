import math
from sys import stdin

# Function to find the GCD of an array
def find_gcd_of_array(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

# Read input from stdin
n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().strip().split()))

# Check if the GCD of the entire array is 1
gcd_array = find_gcd_of_array(array)

# If the GCD of the entire array is 1, we can make all elements equal to 1
if gcd_array == 1:
    print(n - 1)  # At most n-1 operations needed
else:
    print(-1)  # If GCD is not 1, it's impossible to make all elements equal to 1
