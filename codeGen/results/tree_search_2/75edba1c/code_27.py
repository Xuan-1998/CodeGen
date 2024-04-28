N = int(input())  # Read N from input
K = int(input())  # Read K from input
Arr = list(map(int, input().split()))  # Read array elements from input

print(find_subarrays(N, K, Arr))  # Print the result
