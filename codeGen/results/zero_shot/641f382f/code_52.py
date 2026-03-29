from math import gcd
from sys import stdin

# Function to find the GCD of two numbers
def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to find the longest subsequence with GCD 1
def longest_subseq_gcd_one(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == 1:
            return n  # If any element is 1, the longest subsequence is the array itself
        for j in range(i + 1, n):
            current_gcd = find_gcd(current_gcd, arr[j])
            if current_gcd == 1:
                max_len = max(max_len, j - i + 1)
                break
    return max_len

# Main function to solve the problem
def min_operations_to_make_all_elements_one(n, arr):
    overall_gcd = arr[0]
    for num in arr[1:]:
        overall_gcd = find_gcd(overall_gcd, num)
    
    if overall_gcd > 1:
        return -1
    
    longest_subseq_len = longest_subseq_gcd_one(arr)
    return n - longest_subseq_len

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Print the result to stdout
print(min_operations_to_make_all_elements_one(n, arr))
